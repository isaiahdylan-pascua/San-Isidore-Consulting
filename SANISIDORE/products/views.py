from django.shortcuts import render
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
    return render(request, "products/Order.html")