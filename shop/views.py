from django.shortcuts import render
from django.http import HttpResponse
from market.models import Products

def home(request):
    allproducts=Products.objects.all().filter(product_id=1)
    return render(request,'home.html',{'allproducts':allproducts})