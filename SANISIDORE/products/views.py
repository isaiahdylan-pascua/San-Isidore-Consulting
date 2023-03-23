from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import *
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
    if request.method == "POST":
        server = request.POST.get('server')
        table = request.POST.get('table')
        PO = request.POST.get('PO')
        PWDS = request.POST.get('pwds')
        
        new_ord = Order(Server=server, Table=table, PaymentOption=PO, PWDS=PWDS)
        new_ord.save()


    return render(request, "products/Order.html")