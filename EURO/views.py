from django.shortcuts import render
from django.http import JsonResponse
import requests
from Currency.models import CurrencyDetailModel,CurrencyBaseModel
from .models import EuroBank
from bs4 import BeautifulSoup
# Create your views here.



def returnBank():
    rs = requests.get("https://kur.doviz.com/serbest-piyasa/euro")
    bs = BeautifulSoup(rs.content, 'html.parser')

    tables = bs.find_all('table')
    changeRates = list()
    bankValues = list()

    changeTable = tables[0]
    cells = (changeTable.find('tbody')).find_all('td')
    title = ["","Günlük Değşim","Haftalık Değişim","Yıllık Değişim"]
    for i in range(1,4):
        ob = CurrencyBaseModel(title[i], cells[i].get_text(),cells[i].get_attribute_list('class')[0].split('-')[1])
        changeRates.append(ob)

    bankTable = tables[1]

    lines = bankTable.find_all('tr')

    for line in lines:
        cells = line.find_all('td')
        if len(cells) < 1 :
            continue

        ob = EuroBank((cells[0].find('a')).get_text(),cells[1].get_text(),cells[2].get_text())
        bankValues.append(ob)

    bankTable = tables[2]

    lines = bankTable.find_all('tr')

    for line in lines:
        cells = line.find_all('td')
        if len(cells) < 1:
            continue

        ob = EuroBank((cells[0].find('a')).get_text(), cells[1].get_text(), cells[2].get_text())
        bankValues.append(ob)


    return changeRates,bankValues


changeList, bankList = returnBank()
changeRates = list()
bankValues = list()

for ob in changeList:
    ls = {}
    ls['name'] = ob.name
    ls['value'] = ob.value
    ls['type'] = ob.type
    changeRates.append(ls)
print(changeRates)

for ob in bankList:
    ls = {}
    ls['bankName'] = ob.bankName
    ls['buy'] = ob.buy
    ls['sell'] = ob.sell
    bankValues.append(ls)


def lastData(request):
    global changeRates,bankValues
    return JsonResponse([changeRates,bankValues],safe=False,json_dumps_params={'ensure_ascii': False})






