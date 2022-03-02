from django.contrib import admin
from .models import User,StoreMerchant,StoreDriver,Merchant
# Register your models here.
admin.site.register(User)
admin.site.register(StoreMerchant)
admin.site.register(Merchant)
admin.site.register(StoreDriver)