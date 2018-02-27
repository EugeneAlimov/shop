from django.db import models


# Create your models here


class ProductCategory(models.Model):
    name_of_category = models.CharField(max_length=64, blank=True, null=True, default=None,
                                        verbose_name='Наименование категории')
    name_of_product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True, default=None,
                                        verbose_name='Наименование товара')
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


#         модель класса, который еще не был определен нужно вставлять как строку 'модель'


class Product(models.Model):
    name_of_product = models.CharField(max_length=64, blank=True, null=True, default=None,
                                       verbose_name='Наименование товара')
    category = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, verbose_name='Цена')
    currency = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Валюта')
    quantity = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Норма отпуска')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.name_of_product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Quantity(models.Model):
    quantity = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Норма отпуска')

    def __str__(self):
        return "%s" % self.quantity

    class Meta:
        verbose_name = 'Норма отпуска'
        verbose_name_plural = 'Норма отпуска'


class Currency(models.Model):
    currency = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Валюта')

    def __str__(self):
        return "%s" % self.currency

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'


class Status(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Отображать')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                 verbose_name='Категория')
    name_of_product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                        verbose_name='Наименование товара')

    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.is_active

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class Image(models.Model):
    name_of_product_image = models.CharField(max_length=64, blank=True, null=True, default=None,
                                             verbose_name='Наименование изображения товара')
    name_of_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                        verbose_name='Наименование товара')

    product_image = models.ImageField(verbose_name='Изображение', upload_to='static/media/goods_images')
    is_main = models.BooleanField(default=False, verbose_name='Основное')
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлено')

    def __str__(self):
        return "%s" % self.product_image

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
