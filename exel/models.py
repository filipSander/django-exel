from django.db import models



class Product(models.Model):
    name = models.CharField("Наименование", max_length=300)
    place = models.CharField("Область применения", max_length=300)
    facturer = models.CharField("Производитель", max_length=150)
    facturer_сountry = models.CharField("Страна производителя", max_length=150, default="")
    descripton = models.CharField("Примечания", max_length=300)
    image = models.ImageField("Картинка", upload_to="images/")  
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.id}/change'
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"