from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here


class ProductCategory(models.Model):
    name_category = models.CharField(max_length=64, blank=True, null=True,
                                     default=None, verbose_name='Наименование категории')
    category_description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    # image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.name_category

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


#         модель класса, который еще не был определен нужно вставлять как строку 'модель'


class Product(models.Model):
    name_of_goods = models.CharField(max_length=64, blank=True, null=True, default=None,
                                     verbose_name='Наименование товара')
    name_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True,
                                      verbose_name='Наименование категории')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, verbose_name='Цена')
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, verbose_name='Остаток')
    leave_rate = models.ForeignKey('Quantity', on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                   verbose_name='Норма отпуска')
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                 verbose_name='Валюта')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    is_active = models.BooleanField(default=True, verbose_name='Отображать')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.name_of_goods

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Options(models.Model):
    goods_options_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                         verbose_name='Свойство')
    goods_options = models.TextField(blank=True, null=True, default=None, verbose_name='Детали')

    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлен')

    def __str__(self):
        return "%s" % self.goods_options

    class Meta:
        verbose_name = 'Детали'
        verbose_name_plural = 'Детали'


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


class Image(models.Model):
    name_of_product_image = models.CharField(max_length=64, blank=True, null=True, default=None,
                                             verbose_name='Наименование изображения товара')
    name_of_goods = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                      verbose_name='Наименование товара')
    product_image = models.ImageField(verbose_name='Изображение', upload_to='static/media/goods_images/%Y/%m/%d')
    is_main = models.BooleanField(default=False, verbose_name='Основное')
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлено')

    def __str__(self):
        return "%s" % self.product_image

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
