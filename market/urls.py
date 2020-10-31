from django.urls import path
from .views import *

urlpatterns = [
    path('all', market, name='market'),
    path('all/<email>', market, name='market'),
    path('mycart/<email>',my_cart,name='cart'),
    path('addToCart/<email>/<int:pid>', add_to_cart, name="addToCart"),
    path('removeProduct/<email>/<pname>', remove_product, name='removeProduct'),
    path('buy_now',buy_now,name='buy'),
]