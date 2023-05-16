from django.contrib import admin
from .models import Product
admin.site.register(Product)

from .models import Orders
admin.site.register(Orders)

from .models import Orderlines
admin.site.register(Orderlines)
# Register your models here.

from .models import Employee
admin.site.register(Employee)
