from django.contrib import admin
from .models import  Products,ProductType

    
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','product_price','product_details']


admin.site.register(Products,ProductAdmin)
admin.site.register(ProductType)
