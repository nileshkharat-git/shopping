from django.contrib import admin
from .models import Accounts, UserAddress

class AddressAdmin(admin.ModelAdmin):
    list_display=['email','name','house_no','area','city','state','pincode']

admin.site.register(Accounts)
admin.site.register(UserAddress,AddressAdmin)
