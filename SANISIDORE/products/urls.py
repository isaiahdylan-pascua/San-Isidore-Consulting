from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('addProduct', views.addProduct, name='addProduct')
]
