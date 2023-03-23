from django.contrib import admin
from .models import Product
admin.site.register(Product)

from .models import Orders
admin.site.register(Orders)

from .models import test
admin.site.register(test)

# from .models import Orderline
# admin.site.register(Orderline)
# Register your models here.
