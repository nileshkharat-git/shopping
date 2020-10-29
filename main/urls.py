from django.urls import path
from .views import *
urlpatterns = [
    path('sign', cust_signup, name='sign'),
    path('login', cust_login, name='login'),
    path('logout',cust_logout,name='logout')
]