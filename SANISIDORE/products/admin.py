from django.contrib import admin
from .models import Product
admin.site.register(Product)

<<<<<<< Updated upstream
# Register your models here.
=======
from .models import Orders
admin.site.register(Orders)

from .models import Orderlines
admin.site.register(Orderlines)
# Register your models here.

from .models import User
admin.site.register(User)
>>>>>>> Stashed changes
