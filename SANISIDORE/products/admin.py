from django.contrib import admin
from .models import Product
admin.site.register(Product)

from .models import Order
admin.site.register(Order)
# Register your models here.
