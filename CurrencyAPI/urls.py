"""CurrencyAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Currency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('all',views.sendAll,name = "index"),
    path('summary',views.sendSummary,name = "index"),
    path('euro/',include('EURO.urls'),name = 'euro'),
    path('usd/',include('USD.urls'),name = 'usd'),
    path('gbp/',include('GBP.urls'),name = 'gbp'),
    path('gold/',include('GOLD.urls'),name = 'gold'),
    #path('bank/',include('BANK.urls'),name = 'bank'),
]
