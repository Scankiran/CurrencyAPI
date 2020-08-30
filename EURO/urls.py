from django.contrib import admin
from django.urls import path,include

from . import views

app_name = "EURO"

urlpatterns = [
    path('last/', views.lastData, name = 'euroLast'),
    # path('hourly/',views.hourlyData, name = 'euroHourly'),
    # path('daily/',views.dailyData,name='euroDaily'),
    # path('mounthly',views.mounthlyData,name = 'euroMonthly'),
]