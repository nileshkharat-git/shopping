from django.contrib import admin
from .models import  Products,ProductType,MyCart

    
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','product_type','product_price','product_details']

class TypeAdmin(admin.ModelAdmin):
    list_display=['id','p_type']

admin.site.register(Products,ProductAdmin)
admin.site.register(ProductType,TypeAdmin)
admin.site.register(MyCart)
