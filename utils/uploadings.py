import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project_settings'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import django
django.setup()

from exel.models import Product
import xlrd

# class UploadFile(object):
    
#     model = Product

#     def __init__(self, data) -> None:
#         data = data
#         self.uploaded_file = data.get("file")
#         self.parsing()

#     def parsing():
#         return True
    

def uploadFile(data):
    data = data
    uploaded_file = data.get("file")
    return True