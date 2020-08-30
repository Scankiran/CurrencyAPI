from django.contrib import admin
from .models import GOLDMain,GOLDDaily,GOLDHourly,GOLDMonthly
# Register your models here.

admin.site.register(GOLDHourly)
admin.site.register(GOLDDaily)
admin.site.register(GOLDMonthly)
admin.site.register(GOLDMain)
