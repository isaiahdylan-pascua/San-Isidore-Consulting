from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('displayProduct', views.displayProduct, name='displayProduct'),
    path('Order', views.Order, name='Order'),
    path('Orderline', views.Orderline, name='Orderline'),
    path('Receipt', views.Receipt, name='Receipt'),
    path('Delete', views.Delete, name='Delete'),
    path('Stock', views.Stock, name='Stock')
]