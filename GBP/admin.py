from django.contrib import admin
from .models import GBPMain,GBPDaily,GBPHourly,GBPMonthly
# Register your models here.

admin.site.register(GBPHourly)
admin.site.register(GBPMonthly)
admin.site.register(GBPMain)
admin.site.register(GBPDaily)
