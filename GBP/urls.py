from django.contrib import admin
from django.urls import path,include

from . import views

app_name = "GBP"

urlpatterns = [
    path('last/', views.lastData, name = 'gbpLast'),
    # path('hourly/',views.dashboard, name = 'gbpHourly'),
    # path('daily/',views.addArticle,name='gbpoDaily'),
    # path('mounthly',views.detailArticle,name = 'gbpMonthly'),
]