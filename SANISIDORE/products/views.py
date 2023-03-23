from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Product, Orders
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
    if len(Orders.objects.all()) > 1:
        orderno = Orders.objects.order_by('-OrderID')[0].getID
    else:
        orderno = 0
    if request.method == "POST":
        server = request.POST['server']
        table = request.POST['table']
        PO = request.POST['PO']
        PWDS = request.POST['pwds']
        
        new_order = Orders(Server=server,Table=table, PaymentOption=PO, PWDS=PWDS)
        new_order.save()



    return render(request, "products/Order.html", {'orderno': orderno})

# def Orderline(request):
#     orderno = Orders.objects.order_by('-OrderID')[0].getID
#     if request.method == "POST":
#         orderid = orderno
#         pID = request.POST['ItemID']
#         pqty = request.POST['qty']
#         dsc = request.POST['dsc']

#         new_orderline = Orderlines(OrderID=orderid, ProductID=pID, ProductQty=pqty, Discount=dsc)
#         new_orderline.save()

#     return render(request, "products/Order.html")