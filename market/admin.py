from django.contrib import admin
from .models import  Products,ProductType,MyCart

    
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','product_type','product_price','product_details']

class TypeAdmin(admin.ModelAdmin):
    list_display=['id','p_type']

class CartAdmin(admin.ModelAdmin):
    list_filter = ['purchesed']
    list_display = ('user', 'product_name', 'quantity', 'total', 'payment_method', 'purchesed', 'address','status')
    
admin.site.register(Products,ProductAdmin)
admin.site.register(ProductType,TypeAdmin)
admin.site.register(MyCart,CartAdmin)
