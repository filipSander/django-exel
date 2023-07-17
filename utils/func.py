from datetime import date
import io
import os
import sys
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook


os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project_settings'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import django
django.setup()

from exel.models import Product
import openpyxl

    

def uploadFile(data):
    data = data
    uploaded_file = data.get("file")
    
    workbook = openpyxl.open(uploaded_file)
    sheet = workbook.active

    products_bulk_lust = list()
    ids = []

    for row in sheet.iter_rows():
        
        if row[0].data_type == 'n' and row[1].data_type == 's':
            products = Product.objects.filter(name=row[1].value)
            if len(products) == 0:
                print('create product ' + row[1].value)
                newProduct = Product()
                newProduct.name = row[1].value
                products_bulk_lust.append(newProduct)
            else:
                for p in products:
                    ids.append(p.id)
        else:
            continue

    Product.objects.bulk_create(products_bulk_lust)
    for p in products_bulk_lust:
        ids.append(p.id)
    return ids

def getProducts(product_ids):
    products = []
    for id in product_ids:
        try:
            products.append(Product.objects.get(pk=id))
        except: 
            print("Продукт не найден")
    return products


def changeProdcut(data):

    product = Product.objects.get(pk=data.get('id'))
    product.name = data.get('name')
    
    img = data.get("file")
    print(img)
    if img != None:
        product.image = img
  
    product.place = data.get('place')
    product.facturer = data.get('facturer')
    product.facturer_сountry = data.get('facturer_сountry')
    product.descripton = data.get('descripton')
    product.save()
    return True

def createExlx(product_ids):

    output = io.BytesIO()

    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    products = getProducts(product_ids)
    i = 1
    for p in products:
        j = 0
        for attr in p.getAttr():
            worksheet.write(i, j, attr)
            j+=1
        i+=1
    worksheet.write(0, 0, 'Наименование')
    worksheet.write(0, 1, 'Область применения')
    worksheet.write(0, 2, 'Картинка')
    worksheet.write(0, 3, 'Производитель')
    worksheet.write(0, 4, 'Страна Производителя')
    worksheet.write(0, 5, 'Описание')

    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=output.xlsx"

    output.close()
    return response
