from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.



def products(request):
    return render(request, "products/ProductListPrototype.html")

def addProduct(request):
    if request.method == "POST":
        prodname = request.POST['name']
        prodprice = request.POST['price']
        
        new_prod = Product(ProductName=prodname, ProductCost=prodprice)
        new_prod.save()
    
    return render(request, "products/ProductListPrototype.html")

def displayProduct(request):

    data = serializers.serialize("python", Product.objects.all())

    return render(request, "products/ProductListPrototype.html", context={'data'= data})