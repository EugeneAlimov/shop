from django.contrib import admin
from products.models import *


# Register your models here
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    # date_hierarchy = 'name_of_product'
    list_display_links = ['name_of_product', 'name_of_category']


admin.site.register(ProductCategory, ProductCategoryAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    # list_display_links = ['name_of_product']


admin.site.register(Status, StatusAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_display_links = ['name_of_product', 'category']


admin.site.register(Product, ProductAdmin)
