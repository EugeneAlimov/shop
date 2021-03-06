# Generated by Django 2.0.2 on 2018-02-02 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productcategory_name_of_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name_of_product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Наименование товара'),
        ),
    ]
