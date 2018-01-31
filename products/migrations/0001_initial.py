# Generated by Django 2.0.1 on 2018-01-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Наименование товара')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'В наличии',
                'verbose_name_plural': 'В наличии',
            },
        ),
    ]