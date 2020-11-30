from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
from .models import Products, MyCart
from main.models import Accounts,UserAddress

def market(request,email=None):
    allproducts = Products.objects.all()
    return render(request,'market/main.html',{'allproducts':allproducts,'email':email})


def my_cart(request,email):
    cart = MyCart.objects.all().filter(user=email,purchesed=False)
    allproducts = list()
    for product in cart:
        allproducts.append(Products.objects.filter(product_name=product.product_name))
    return render(request,'mycart.html',{'cart':allproducts,'email':email})

@login_required(login_url='/accounts/login')    
def add_to_cart(request, email, pid):
    user=Accounts.objects.get(email=email)
    product=Products.objects.get(product_id=pid)
    MyCart(user=user, product_name=product, quantity=1, total=product.product_price).save()
    return redirect(my_cart,user.email)
    
def remove_product(request, email, pid):
    product=MyCart.objects.filter(user=Accounts.objects.get(email=email),product_name=pid)
    product.delete()
    success(request,"Product removed successfully.")
    return redirect(my_cart,email)
    
@login_required(login_url='/accounts/login')    
def buy_now(request, pid=None, email=None):
    product=Products.objects.get(product_id=pid)
    quantity = MyCart.objects.get(user=Accounts.objects.get(email=email), product_name=product).quantity
    context={'product':product,'quantity':quantity,'email':email}
    return render(request, 'buy.html', context)
    
def payment_getway(request,pid=None):
    if request.POST:
        payment = request.POST['payment']
        email = request.POST['email']
        pid = request.POST['product']
        cart = MyCart.objects.filter(user=email, product_name=pid).get()
        address = UserAddress.objects.filter(email=email,useDefault=True).get()
        cart.purchesed = True
        cart.payment_method = payment
        cart.address = address
        cart.status='OP'
        cart.save()
        return redirect('/')
    return render(request,"payment.html")

def offer(request,ptype):
    url = "offer/clothOffer.html"
    return render(request, url)
    
