from django.contrib import admin
from .models import USDMain,USDDaily,USDHourly,USDMonthly
# Register your models here.

admin.site.register(USDDaily)
admin.site.register(USDMonthly)
admin.site.register(USDHourly)
admin.site.register(USDMain)
