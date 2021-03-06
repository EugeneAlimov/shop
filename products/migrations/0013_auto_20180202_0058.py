# Generated by Django 2.0.2 on 2018-02-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20180131_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Отображать', 'verbose_name_plural': 'Отображать'},
        ),
        migrations.RemoveField(
            model_name='status',
            name='created',
        ),
        migrations.RemoveField(
            model_name='status',
            name='updated',
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='status',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отображать'),
        ),
    ]
