from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# from products.forms import MyForm

from products.models import *


# Create your views here.
def goods_adding(request):
    return_dict = dict()
    data = request.POST

    name_of_goods = data.get('name_of_goods')
    price = data.get('price')
    name_category = data.get('name_of_category')
    goods_description = data.get('goods_description')
    goods_short_description = data.get('goods_short_description')
    image = data.get('image')

    category_description = data.get('category_description')
    category_short_description = data.get('category_short_description')

    qqq = ProductCategory(name_of_category=name_category, description=category_description, )

    qqq.save()

    dsg = Product(name_of_product=name_of_goods, price=price, short_description=goods_short_description,
                  description=goods_description, )

    dsg.save()

    return JsonResponse(return_dict)


def category_adding(request):
    return_dict = dict()
    return JsonResponse(return_dict)


def management(request):
    print('Ololo xyi')
    return render(request, 'management/management.html')
