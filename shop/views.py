from django.shortcuts import render, redirect
from market.models import Products, ProductType, MyCart


def home(request):
    product_types = ProductType.objects.all()
    titles = dict()
    for ptype in product_types:
        titles[ptype.id] = ptype
    return render(request, 'home.html', {'titles': titles})

def cloth_offer(request, ptype=None):
    items = Products.objects.all().filter(product_type=ptype)
    email=request.POST['email']
    return render(request,"offer/clothOffer.html",{'items':items,'email':email})

