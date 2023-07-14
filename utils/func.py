import os
import sys

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

def getProducts(ids):
    products = []
    if len(ids) > 0:
        for id in ids:
            try:
                products.append(Product.objects.get(pk=id))
            except: 
                print("Продукт не найден")