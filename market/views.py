from django.shortcuts import render,redirect
from django.contrib.messages import success
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
    product=MyCart.objects.filter(user=Accounts.objects.get(email=email),product_name=pname)
    product.delete()
    success(request,"Product removed successfully.")
    return redirect(my_cart,email)
    
@login_required(login_url='/accounts/login')    
def buy_now(request, pid=None, email=None):
    product=Products.objects.get(product_id=pid)
    quantity = MyCart.objects.get(user=Accounts.objects.get(email=email), product_name=product.product_name).quantity
    context={'product':product,'quantity':quantity,'email':email}
    return render(request, 'buy.html', context)
    
def payment_getway(request,product_name):
    if request.POST:
        payment = request.POST['payment']
        email = request.POST['email']
        cart = MyCart.objects.get(user=Accounts.objects.get(email=email), product_name=product_name)
        cart.purchesed = True
        cart.payment_method = payment
        cart.save()
        print(cart.user)
        return redirect('/')
    return render(request,"payment.html")

def offer(request,ptype):
    url = "offer/clothOffer.html"
    return render(request,url)