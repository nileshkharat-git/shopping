from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/',include('main.urls')),
    path('market/', include('market.urls')),
    path('offer/<ptype>',cloth_offer,name="offer"),
    path('payment',payment,name="payment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)