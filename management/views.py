from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from products.forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from products.models import *


# def goods_adding(request):
#     print('sda')
#     if request.method == 'POST' and request.FILES['image']:
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

# Create
# your
# views
# here.


def goods_adding(request):
    print("form good adding !!!!!!!!!")
    return_dict = dict()
    data = request.POST
    # image = request.FILES
    name_of_goods = data.get('name_of_goods')
    price = data.get('price')
    goods_description = data.get('goods_description')
    goods_short_description = data.get('goods_short_description')

    dsg = Product(name_of_product=name_of_goods, price=price, short_description=goods_short_description,
                  description=goods_description)
    # www = Product(product_image_name=image)
    # print(image)
    print(price)
    print(name_of_goods)
    dsg.save()
    # # www.save()

    return JsonResponse(return_dict)


def category_adding(request):
    return_dict = dict()
    data = request.POST
    name_category = data.get('name_of_category')
    category_description = data.get('category_description')
    category_short_description = data.get('category_short_description')

    qqq = ProductCategory(name_of_category=name_category, description=category_description,
                          short_description=category_short_description)

    qqq.save()

    print("form category adding !!!!!!!!!")

    return JsonResponse(return_dict)


def management(request):
    name_category_list = ProductCategory.objects.all()
    print(name_category_list)
    return render(request, 'management/management.html', {'name_category_list': name_category_list})
