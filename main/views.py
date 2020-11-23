from django.shortcuts import render, redirect
from django.contrib.messages import success,info,error,warning
from django.contrib.auth import authenticate,login,logout
from .forms import MyForm, LogForm
from .models import Accounts,UserAddress

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

def add_location(request):
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
    return render(request,"addLocation.html")