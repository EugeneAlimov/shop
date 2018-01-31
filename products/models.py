from django.db import models


# Create your models here


class ProductCategory(models.Model):
    name_of_category = models.CharField(max_length=64, blank=True, null=True, default=None,
                                       verbose_name='Наименование категории')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.name_of_category

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name_of_product = models.CharField(max_length=64, blank=True, null=True, default=None,
                                       verbose_name='Наименование товара')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                 verbose_name='Категория')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'


class Status(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.is_active

    class Meta:
        verbose_name = 'В наличии'
        verbose_name_plural = 'В наличии'
