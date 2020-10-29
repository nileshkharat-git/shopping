from django.urls import path
from .views import *
urlpatterns = [
    path('sign',cust_signup,name='sign'),
]