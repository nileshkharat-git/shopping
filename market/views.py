from django.shortcuts import render
from .models import Products

def market(request):
    allproducts = Products.objects.all()
    return render(request,'market/main.html',{'allproducts':allproducts})
