from django.contrib import admin
from products.models import *


# Register your models here
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    list_display_links = ['name_category']


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_display_links = ['name_of_goods']


admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Image._meta.fields]
    list_display_links = ['product_image']


admin.site.register(Image, ImageAdmin)


class OptionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Options._meta.fields]
    list_display_links = ['goods_options']


admin.site.register(Options, OptionsAdmin)


class QuantityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Quantity._meta.fields]


admin.site.register(Quantity, QuantityAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields]


admin.site.register(Currency, CurrencyAdmin)
