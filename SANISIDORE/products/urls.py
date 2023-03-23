from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('displayProduct', views.displayProduct, name='displayProduct'),
    path('Order', views.Order, name='Order'),
]