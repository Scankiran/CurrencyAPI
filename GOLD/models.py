from django.db import models

# Create your models here.
class GOLDMain(models.Model):
    name = models.CharField(max_length=50, verbose_name="mainData")
    value = models.CharField(max_length=50, verbose_name="mainValue")
    changeRate = models.CharField(max_length=50, verbose_name="mainChangeRate")
    changeType = models.CharField(max_length=50, verbose_name="mainChangeType")
    date = models.DateTimeField(auto_now_add=True)


class GOLDDaily(models.Model):
    date = models.CharField(max_length=50,verbose_name="dailyDate")
    name = models.CharField(max_length=50, verbose_name="dailyData")
    value = models.CharField(max_length=50, verbose_name="dailyValue")
    changeRate = models.CharField(max_length=50, verbose_name="dailyChangeRate")
    changeType = models.CharField(max_length=50, verbose_name="dailyChangeType")
    date = models.DateTimeField(auto_now_add=True)


class GOLDHourly(models.Model):
    date = models.CharField(max_length=50,verbose_name="hourlyDate")
    name = models.CharField(max_length=50, verbose_name="hourlyData")
    value = models.CharField(max_length=50, verbose_name="hourlyValue")
    changeRate = models.CharField(max_length=50, verbose_name="hourlyChangeRate")
    changeType = models.CharField(max_length=50, verbose_name="hourlyChangeType")
    date = models.DateTimeField(auto_now_add=True)


class GOLDMonthly(models.Model):
    date = models.CharField(max_length=50,verbose_name="monthlyDate")
    name = models.CharField(max_length=50, verbose_name="monthlyData")
    value = models.CharField(max_length=50, verbose_name="monthlyValue")
    changeRate = models.CharField(max_length=50, verbose_name="monthlyChangeRate")
    changeType = models.CharField(max_length=50, verbose_name="monthlyChangeType")
    date = models.DateTimeField(auto_now_add=True)