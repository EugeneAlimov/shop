# Generated by Django 2.0.1 on 2018-01-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='name_of_product',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Наименование товара'),
        ),
    ]
