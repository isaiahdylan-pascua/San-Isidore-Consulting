from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Product, Orders, Orderlines
from django.contrib import messages
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
        
        new_prod = Product(ProductName=prodname, ProductCost=prodprice)
        new_prod.save()
    
    return render(request, "products/ProductListPrototype.html", {'products': products})

def displayProduct(request):
    products = Product.objects.all()
    return render(request, "products/test.html", {'products': products})

def Order(request):
    #List of all products
    products = Product.objects.all()

    #If Order list is empty, assign 0 to orderno
    if len(Orders.objects.all()) > 0:
        orderno = Orders.objects.order_by('-OrderID')[0].pk
    else:
        orderno = 0

    #Orderline with the highest pk, otherwise known as current list of ordered products
    ol = Orderlines.objects.filter(OrderID=orderno)

    if request.method == "POST":
        server = request.POST['server']
        table = request.POST['table']
        PO = request.POST['PO']
        PWDS = request.POST['pwds']

        edit_order = Orders.objects.get(pk=orderno)
        edit_order.Server = server
        edit_order.Table = table
        edit_order.PaymentOption = PO
        edit_order.PWDS = PWDS
        edit_order.save()
        
        
        new_order = Orders()
        new_order.save()
        messages.info(request, 'Generating Receipt')
        return redirect('Receipt')



    return render(request, "products/Order.html", 
    {'orderno': orderno, 
    'products': products, 
    'ol':ol
    })

def Orderline(request):
    products = Product.objects.all()
    if len(Orders.objects.all()) > 0:
        orderno = Orders.objects.order_by('-OrderID')[0].pk
    else:
        orderno = 0
    ol = Orderlines.objects.filter(OrderID=orderno)
    if request.method == "POST":
        orderid = orderno
        P = request.POST['Product']
        pqty = request.POST['qty']
        dsc = request.POST['dsc']
        Pdesc = Product.objects.get(ProductID=P).ProductName
        PCost = int(Product.objects.filter(ProductID=P)[0].ProductCost)

        if dsc == 'True':
            FP = 0
        else:
            FP = int(pqty)*PCost



        new_orderline = Orderlines(OrderID=orderid, Product=P, ProductCost=PCost, ProductQty=pqty, Discount=dsc, ProductDesc=Pdesc, Finalprice=FP)
        new_orderline.save()


    return render(request, "products/Order.html", 
    {
        'orderno': orderno, 
        'products': products, 
        'ol':ol
    })

def Receipt(request):
    orderno = Orders.objects.order_by('-OrderID')[1]
    ol = Orderlines.objects.filter(OrderID=Orders.objects.order_by('-OrderID')[1].pk)
    subtotal = 0
    pwds = 0
    for x in ol:
        subtotal = subtotal + x.Finalprice
    
    if orderno.PWDS == 'True':
        pwds = subtotal*.2
    
    total = subtotal - pwds
    
    # if request.method == "POST":
    #     # server = request.POST['server']
    #     # table = request.POST['table']
    #     # PO = request.POST['PO']
    #     # PWDS = request.POST['pwds']

    #     # edit_order = Orders.objects.get(pk=orderno.pk)
    #     # edit_order.Server = server
    #     # edit_order.Table = table
    #     # edit_order.PaymentOption = PO
    #     # edit_order.PWDS = PWDS
    #     # edit_order.save()

    #     new_order = Orders()
    #     new_order.save()
    #     messages.info(request, 'Generating Receipt')
    #     return redirect('Receipt')

    


    return render(request, "products/Receipt.html", 
    {
        'orderno': orderno,  
        'ol':ol,
        'subtotal':subtotal,
        'pwds':pwds,
        'total':total

    })