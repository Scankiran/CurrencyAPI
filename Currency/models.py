from django.db import models
# Create your models here.

class CurrencyBaseModel:
    def __init__(self,name,value,type):
        self.name = name
        self.value = value
        self.type = type


class CurrencyDetailModel:
    def __init__(self,name,buy,sell,max,min,type):
        self.name = name
        self.buy = buy
        self.sell = sell
        self.max = min
        self.min = max
        self.type = type
