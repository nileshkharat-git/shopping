from django.shortcuts import render, redirect
from django.contrib.messages import success,info,error,warning
from django.contrib.auth import authenticate,login,logout
from .forms import MyForm,LogForm

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
    return redirect('/')