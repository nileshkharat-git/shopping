from django.shortcuts import render,redirect
from .forms import MyForm

def cust_signup(request):
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'sign.html',{'form':form})