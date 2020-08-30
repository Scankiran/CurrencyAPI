from django.contrib import admin
from .models import BANKMain,BANKDaily,BANKHourly,BANKMonthly
# Register your models here.
admin.site.register(BANKMain)
admin.site.register(BANKHourly)
admin.site.register(BANKDaily)
admin.site.register(BANKMonthly)