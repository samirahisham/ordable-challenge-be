from django.contrib import admin

# Register your models here.
from .models import Store,Item,Order,OrderItems
# Register your models here.
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItems)