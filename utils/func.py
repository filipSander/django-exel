from datetime import date, timezone
import io
import os
import sys
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook

from app.settings import BASE_DIR, TEMPLATE_TEXT


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
        if row[0].data_type == 'n' and row[1].data_type == 's' and row[5].data_type == 's':
            products = Product.objects.filter(name=row[1].value)
            if len(products) == 0:
                print('create product ' + row[1].value)
                newProduct = Product()
                newProduct.name = row[1].value
                newProduct.facturer = row[5].value

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
    worksheet.set_column(0, 1, 12)
    cell_format = workbook.add_format({
        'border':   1,
    })

    header_format = workbook.add_format({
        'border':   1,
    })
    cell_format.set_text_wrap()
    cell_format.set_align('top')

    header_format.set_text_wrap()
    header_format.set_align('top')
    worksheet.set_column(2, 4, 20)

    merge_format = workbook.add_format({    
        'align': 'center',
        'valign': 'vcenter',
        })
    merge_format.set_text_wrap()
    worksheet.merge_range('A1:F8', TEMPLATE_TEXT, merge_format)
    products = getProducts(product_ids)
    i = 9
    for p in products:
        j = 0
        for attr in p.getAttr():
            if j == 0 and attr != '':
                worksheet.write(i, j, "", cell_format)
                worksheet.insert_image(i, j, str(BASE_DIR) + "\\" + attr, {"x_scale": 1, "y_scale": 1,"x_offset": 1, "y_offset": 1})
            else:
                worksheet.write(i, j, attr, cell_format)
            j+=1
            worksheet.set_row(i, 80) 
        i+=1
    header_format.set_align('center')
    header_format.set_align('vcenter')
    worksheet.write(8, 0, 'Фото', header_format)
    worksheet.write(8, 1, 'Наименование ', header_format)
    worksheet.write(8, 2, 'Область применения', header_format)
    worksheet.write(8, 3, 'Примечание \n (параметры)', header_format)
    worksheet.write(8, 4, 'Страна производителя', header_format)
    worksheet.write(8, 5, 'Производитель', header_format)

    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=output.xlsx"

    output.close()
    return response

