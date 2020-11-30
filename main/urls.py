from django.urls import path
from .views import *
urlpatterns = [
    path('sign', cust_signup, name='sign'),
    path('login', cust_login, name='login'),
    path('logout', cust_logout, name='logout'),
    path('myaccount', show_dashboard, name='dashboard'),
    path('addAddress/<str:email>', add_location, name='addAddress'),
    path("myorders", my_orders, name='myorders'),
    path('selectAddress',select_address,name='selectAddr')
    
]