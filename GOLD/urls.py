from django.contrib import admin
from django.urls import path,include

from . import views

app_name = "GOLD"

urlpatterns = [
    # path('last/', views.index, name = 'goldLast'),
    # path('hourly/',views.dashboard, name = 'goldHourly'),
    # path('daily/',views.addArticle,name='goldDaily'),
    # path('mounthly/',views.detailArticle,name = 'goldMonthly'),
]