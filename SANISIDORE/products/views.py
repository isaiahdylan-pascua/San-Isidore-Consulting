from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Product, Orders, Orderlines, Stocks
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
# from .models import products


# Create your views here.



def products(request):
    products = Product.objects.all()
    return render(request, "products/ProductListPrototype.html", {'products': products})

def addProduct(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodname = request.POST['name']
        prodprice = request.POST['price']
        new_prod = Product(ProductName=prodname, ProductCost=prodprice, ProductStock=0)
        new_prod.save()

        # Product.objects.create(ProductName=prodname, ProductCost=prodprice)
    
    return render(request, "products/ProductListPrototype.html", {'products': products})

def Stock(request):
    products = Product.objects.all()

    if request.method == "POST":
        Stockitem = request.POST['Product']
        Stockqty = request.POST['stock']
        
        restock = Product.objects.get(ProductID = Stockitem)
        restock.ProductStock = Stockqty
        restock.save()
    return render(request, "products/ProductListPrototype.html", {'products': products})

def displayProduct(request):
    products = Product.objects.all()
    return render(request, "products/test.html", {'products': products})

def Order(request):

    #List of all products
    products = Product.objects.all()

    #If Order list is empty, assign 0 to orderno
    if len(Orders.objects.all()) > 0:
        current_order = Orders.objects.order_by('-OrderID')[0]
        orderno = current_order.pk
    else:
        new_order = Orders()
        new_order.save()
        orderno = 0
        current_order = 0

    #Orderline with the highest pk, otherwise known as current list of ordered products
    ol = Orderlines.objects.filter(OrderID=orderno)
    ol_no = len(ol)

    
    subtotal = 0
    ol2 = Orderlines.objects.filter(OrderID=Orders.objects.order_by('-OrderID')[1].pk)
    for x in ol2:
        subtotal = subtotal + x.Finalprice
    if request.method == "POST":

        server = request.POST['server']
        table = request.POST['table']
        PO = request.POST['PO']
        PWDS = request.POST['pwds']
        T = request.POST['tendered']

        if Decimal(T)<Decimal(subtotal):
            messages.info(request, 'Insufficient Funds')
            return redirect('Order')
        
        else:
            edit_order = Orders.objects.get(pk=orderno)
            edit_order.Server = server
            edit_order.Table = table
            edit_order.PaymentOption = PO
            edit_order.PWDS = PWDS
            edit_order.Tendered = T
            edit_order.save()
            
            
            new_order = Orders()
            new_order.save()
            messages.info(request, 'Generating Receipt')
            return redirect('Receipt')



    return render(request, "products/Order.html", 
    {'orderno': orderno, 
    'current_order':current_order,
    'products': products, 
    'ol':ol,
    'ol_no':ol_no,
    'subtotal':subtotal
    })

def Orderline(request):
    products = Product.objects.all()
    if len(Orders.objects.all()) > 0:
        current_order = Orders.objects.order_by('-OrderID')[0]
        orderno = current_order.pk
    else:
        orderno = 0
        current_order = 0
    ol = Orderlines.objects.filter(OrderID=orderno)
    if request.method == "POST":
        orderid = orderno
        P = request.POST['Product']
        pqty = int(request.POST['qty'])
        dsc = request.POST['dsc']
        Pdesc = Product.objects.get(ProductID=P).ProductName
        Pstock = Product.objects.get(ProductID=P).ProductStock
        PCost = int(Product.objects.filter(ProductID=P)[0].ProductCost)

        if dsc == 'True':
            FP = 0
        else:
            FP = int(pqty)*PCost

        if (Pstock-pqty) < 0:
            messages.error(request, 'Insufficient stock')

        else:
            if len(Orderlines.objects.filter(Product = P, OrderID = orderid)) == 0:
                new_orderline = Orderlines(OrderID=orderid, Product=P, ProductCost=PCost, ProductQty=pqty, Discount=dsc, ProductDesc=Pdesc, Finalprice=FP)
                new_orderline.save()

                stockupdate = Product.objects.get(ProductID=P)
                stockupdate.ProductStock = Pstock - pqty
                stockupdate.save()

                return redirect('Order')
            else:
                edit_orderline = Orderlines.objects.get(Product = P, OrderID = orderid)
                edit_orderline.ProductCost = PCost
                edit_orderline.ProductQty = pqty
                edit_orderline.Discount = dsc
                edit_orderline.ProductDesc = Pdesc
                edit_orderline.Finalprice = FP
                edit_orderline.save()

                stockupdate = Product.objects.get(ProductID=P)
                stockupdate.ProductStock = Pstock - pqty
                stockupdate.save()
                return redirect('Order')   


        return render(request, "products/Order.html", 
    {
        'orderno': orderno, 
        'current_order':current_order,
        'products': products, 
        'ol':ol
    })

def Delete(request):
    products = Product.objects.all()
    if len(Orders.objects.all()) > 0:
        orderno = Orders.objects.order_by('-OrderID')[0].pk
    else:
        orderno = 0
    ol = Orderlines.objects.filter(OrderID=orderno)

    if request.method == "POST":
        orderid = orderno
        P = request.POST['delete']
        close_orderline = Orderlines.objects.get(OrderID=orderno, Product=P)
        close_orderline.delete()
        return redirect('Order')

    return render(request, "products/Order.html", 
    {
        'orderno': orderno, 
        'products': products, 
        'ol':ol
    })

def DeleteProduct(request):
    if request.method == "POST":
        PID = request.POST['delete']
        deleteproduct = Product.objects.get(ProductID=PID)
        deleteproduct.delete()
        return redirect('products')

    return render(request, "products/ProductListPrototype.html",)

def Receipt(request):
    orderno = Orders.objects.order_by('-OrderID')[1]
    ol = Orderlines.objects.filter(OrderID=Orders.objects.order_by('-OrderID')[1].pk)
    subtotal = 0
    pwds = 0
    for x in ol:
        subtotal = subtotal + x.Finalprice
    
    if orderno.PWDS == 'True':
        pwds = Decimal(subtotal)*Decimal(.2)
    
    total = subtotal - pwds

    orderno.OrderTotal = total
    orderno.Date = timezone.now()
    orderno.save()

    
    change = orderno.Tendered - total
    return render(request, "products/Receipt.html", 
    {
        'orderno': orderno,  
        'ol':ol,
        'subtotal':subtotal,
        'pwds':pwds,
        'total':total,
        'change':change

    })

def Salesreport(request):
    O = Orders.objects.latest('OrderID')
    O = Orders.objects.exclude(OrderID=O.OrderID)
    # O = O[len(O)-1]
    if request.method == "POST":
        # Orders = Orders.objects.all()
        Day = request.POST['Daily']
        Month = request.POST['Monthly']
        Year = request.POST['Yearly']
        if Day == "0" and Month == "0":
            O = Orders.objects.filter(Date__year = Year)
            messages.info(request, 'Sales Record as of ' + Year)
        elif Day == "0":
            O = Orders.objects.filter(Date__month = Month, Date__year = Year)
            messages.info(request, 'Sales Record as of ' + Month + '-' + Year)
        else: 
            O = Orders.objects.filter(Date__day = Day, Date__month = Month, Date__year = Year)
            messages.info(request, 'Sales Record as of ' + Day + '-' + Month + '-' + Year)
        # return redirect('Salesreport')



    return render(request, "products/Salesreport.html", 
    {
    'Days':range(1, 32),
    # 'Months':['-', 'January', 'February','March','April','May','June','July','August','September','October','November','December'], 
    'Months':range(1,13),
    'Years':range(2000, 2051),
    'O':O
    }
     
    )

def Index(request):
    return render(request, "products/Index.html")