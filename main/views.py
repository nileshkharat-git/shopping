from django.shortcuts import render, redirect
from django.contrib.messages import success,info,error,warning
from django.contrib.auth import authenticate,login,logout
from .forms import MyForm, LogForm
from .models import Accounts, UserAddress
from market.models import MyCart, Products


def cust_signup(request):
    if request.POST:
        try:
            form=MyForm(request.POST)
            if form.save():
                success(request,"Account create successfully.")
                return redirect(cust_login)
        except Exception:
            error(request,"Please enter valid details.")
    form = MyForm()
    return render(request, 'sign.html', {'form': form})

def cust_login(request):
    form=LogForm(request.POST or None)
    if form.is_valid():
        email = request.POST['email']
        password=request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            info(request, f"Welcome {user.username}")
            print("login success")
            return redirect('/')
    else:
        pass
    return render(request, 'sign.html', {'form': form})
    
def cust_logout(request):
    logout(request)
    return redirect(cust_login)

def show_dashboard(request):
    email = request.POST['email']
    user = Accounts.objects.get(email=email)
    context={'user':user}
    return render(request, "dashBoard.html", context)

def add_location(request,email=None):
    if request.method == "POST":
        user=Accounts.objects.get(email=request.POST['email'])
        name=request.POST['name']
        mobile=request.POST['mobile']
        houseno=request.POST['houseno']
        area=request.POST['area']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        address = UserAddress(email=user,name=name, mobile=mobile, house_no=houseno, area=area, city=city, state=state, pincode=pincode)
        address.save()
        return redirect(add_location)
    locations = UserAddress.objects.all().filter(email=email)
    pid=request.GET['product']
    return render(request, "addLocation.html",{'locations':locations,'product_id':pid})

def my_orders(request):
    if request.method == 'POST':
        if request.path == '/accounts/myorders':
            email = request.POST['email']
            allorders = MyCart.objects.all().filter(user=email, purchesed=True)
            return render(request, 'myOrders.html', {'allorders': allorders})
    return render(request,"myOrders.html")

def select_address(request):
    if request.POST:
        email = request.POST['email']
        name = request.POST['name']
        pid = request.POST['product']
        if UserAddress.objects.filter(email=email, useDefault=True).exists() and UserAddress.objects.filter(email=email, useDefault=True).get().name != name:
            addr = UserAddress.objects.filter(email=email, useDefault=True).get()
            addr.useDefault = False
            addr.save()
        else:
            return render(request,"payment.html",{'product':pid,'email':email})
        if not UserAddress.objects.filter(email=email, name=name).exists():
            error(request, "Selected address is wrong!")
            return redirect(add_location)

        selected = UserAddress.objects.filter(email=email, name=name).get()
        selected.useDefault = True
        selected.save()
        return render(request,"payment.html",{'product':pid,'email':email})
    return redirect(add_location)        
    
    
