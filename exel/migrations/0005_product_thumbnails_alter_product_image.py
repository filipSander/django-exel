# Generated by Django 4.2.3 on 2023-07-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnails',
            field=models.ImageField(blank=True, upload_to='images/thumbs/%Y/%m/%d/', verbose_name='Миниатюра'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/img/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
