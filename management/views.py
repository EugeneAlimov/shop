from django.http import JsonResponse
from django.shortcuts import render
from management.forms import *
from products.models import *


# Create your views here.


def goods_adding(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        for image_list in request.FILES.getlist('product_image'):
            image_load = Image(product_image=image_list)
            print(image_load)
            image_load.save()
    else:
        print('Пусто')

    data = request.POST

    name_of_goods = data.get('name_of_goods')
    price = data.get('price')
    goods_description = data.get('goods_description')
    goods_short_description = data.get('goods_short_description')
    choice_category = data.get('category')
    currency = data.get('currency')
    quantity = data.get('quantity')
    goods_load = Product(name_of_product=name_of_goods, price=price, short_description=goods_short_description,
                         description=goods_description, category=choice_category, currency=currency, quantity=quantity)

    goods_load.save()
    return JsonResponse(data)


def category_adding(request):
    return_dict = dict()
    data = request.POST
    name_category = data.get('name_of_category')
    category_description = data.get('category_description')
    category_short_description = data.get('category_short_description')

    qqq = ProductCategory(name_of_category=name_category, description=category_description,
                          short_description=category_short_description)

    qqq.save()

    return JsonResponse(return_dict)


def management(request):
    name_category_list = ProductCategory.objects.all()
    name_currency_list = Currency.objects.all()
    rate_of_loss_list = Quantity.objects.all()
    return render(request, 'management/management.html', {'name_category_list': name_category_list,
                                                          'rate_of_loss_list': rate_of_loss_list,
                                                          'name_currency_list': name_currency_list})
