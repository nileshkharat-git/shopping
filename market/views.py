from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Products, MyCart
from main.models import Accounts

def market(request,email=None):
    allproducts = Products.objects.all()
    return render(request,'market/main.html',{'allproducts':allproducts,'email':email})


def my_cart(request,email):
    cart = MyCart.objects.all().filter(user=email)
    allproducts = list()
    for product in cart:
        allproducts.append(Products.objects.filter(product_name=product.product_name))
    return render(request,'mycart.html',{'cart':allproducts,'email':email})

@login_required(login_url='/accounts/login')    
def add_to_cart(request, email, pid):
    user=Accounts.objects.get(email=email)
    product=Products.objects.get(product_id=pid)
    MyCart(user=user, product_name=product.product_name, quantity=1, total=product.product_price).save()
    return redirect(my_cart,user.email)
    
def remove_product(request, email, pname):
    product=MyCart(user=Accounts.objects.get(email=email),product_name=pname)
    product.delete()
    return redirect(my_cart,email)
    
def buy_now(request):
    return render(request,'navbar.html')