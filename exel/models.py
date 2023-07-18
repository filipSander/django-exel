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
    image = models.ImageField("Картинка", upload_to="images/%Y/%m/%d/", blank=True)  
    thumbnails = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, 
    verbose_name='Миниатюра')
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.id}/change'
    
    def save(self, **kwargs):
        output_size = (169, 169)
        output_thumb = BytesIO()

        img = Image.open(self.image)
        img_name = self.image.name.split('.')[0]

        if img.height > 169 and img.width > 169:
            img.thumbnail(output_size)
            img.save(output_thumb,format='JPEG',quality=90)
            self.thumbnails = InMemoryUploadedFile(output_thumb, 'ImageField', f"{img_name}_thumb.jpg", 'image/jpeg', sys.getsizeof(output_thumb), None)
        else: 
            self.thumbnails = self.image
        super(Product, self).save()
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def getAttr(self):
        return [
            str(self.thumbnails),
            self.name, 
            self.place, 
            self.descripton, 
            self.facturer_сountry, 
            self.facturer
        ]
    
    