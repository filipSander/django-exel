from io import BytesIO
import sys
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO



class Product(models.Model):
    name = models.CharField("Наименование", max_length=300)
    place = models.CharField("Область применения", max_length=300)
    facturer = models.CharField("Производитель", max_length=150)
    facturer_сountry = models.CharField("Страна производителя", max_length=150, default="")
    
    descripton = models.CharField("Примечание", max_length=300)
    image = models.ImageField("Картинка", upload_to="images/", blank=True)  
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.id}/change'
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def getAttr(self):
        return [
            str(self.image),
            self.name, 
            self.place, 
            self.descripton, 
            self.facturer_сountry, 
            self.facturer
        ]
    
    