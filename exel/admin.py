from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

from exel.models import Product


# Register your models here.


class ProductResource(resources.ModelResource):
    class Meta: 
        model = Product

class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    
admin.site.register(Product, ProductAdmin)