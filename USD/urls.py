from django.contrib import admin
from django.urls import path,include

from . import views

app_name = "USD"

urlpatterns = [
    path('last/', views.lastData, name = 'usdLast'),
    # path('hourly/',views.dashboard, name = 'usdHourly'),
    # path('daily/',views.addArticle,name='usdDaily'),
    # path('mounthly',views.detailArticle,name = 'usdMonthly'),
]