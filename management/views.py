from django.http import JsonResponse
from django.shortcuts import render

from management.forms import *
from products.models import *


# Create your views here.

def goods_adding(request):
    data = request.POST

    name_of_goods = data.get('name_of_goods')
    price = data.get('price')
    goods_description = data.get('goods_description')
    goods_short_description = data.get('goods_short_description')
    choice_category = data.get('category')
    cat = ProductCategory.objects.filter(name_category=choice_category)
    dsg = Product(name_of_goods=name_of_goods, price=price, short_description=goods_short_description,
                  description=goods_description, name_category=cat[0])
    dsg.save()

    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        print('Есть форма')

        name_of_goods_id = Product.objects.get(name_of_goods=name_of_goods)

        for i in request.FILES.getlist('product_image'):
            Image(product_image=i, name_of_product_image=i, name_of_goods=name_of_goods_id).save()

    else:
        print('Пусто')

    return JsonResponse(data)


def category_adding(request):
    return_dict = dict()
    data = request.POST
    name_category = data.get('name_of_category')
    category_description = data.get('category_description')
    category_short_description = data.get('category_short_description')

    qqq = ProductCategory(name_category=name_category, category_description=category_description,
                          short_description=category_short_description)
    qqq.save()

    return JsonResponse(return_dict)


def management(request):
    name_category_list = ProductCategory.objects.all()
    name_quantity_list = Quantity.objects.all()
    name_currency_list = Currency.objects.all()
    return render(request, 'management/management.html',
                  {'name_category_list': name_category_list,
                   'name_quantity_list': name_quantity_list,
                   'name_currency_list': name_currency_list}
                  )
