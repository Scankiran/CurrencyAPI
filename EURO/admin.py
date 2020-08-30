from django.contrib import admin
from .models import EURODaily,EUROHourly,EUROMonthly,EUROMain
# Register your models here.
admin.site.register(EUROHourly)
admin.site.register(EUROMonthly)
admin.site.register(EURODaily)
admin.site.register(EUROMain)