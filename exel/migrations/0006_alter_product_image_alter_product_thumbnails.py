# Generated by Django 4.2.3 on 2023-07-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0005_product_thumbnails_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnails',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Миниатюра'),
        ),
    ]
