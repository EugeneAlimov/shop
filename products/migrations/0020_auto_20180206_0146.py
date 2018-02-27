# Generated by Django 2.0.2 on 2018-02-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Название изображения'),
        ),
        migrations.AlterField(
            model_name='image',
            name='product_image',
            field=models.ImageField(upload_to='static/media/goods_images', verbose_name='Изображение'),
        ),
    ]