from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# from products.forms import MyForm

from products.models import *


# Create your views here.
def goods_adding(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    name_of_goods = data.get('name_of_goods')
    price = data.get('price')

    dsg = Product(name_of_product=name_of_goods, price=price)

    dsg.save()

    return JsonResponse(return_dict)


def goods_adding(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    name_of_goods = data.get('name_of_goods')
    price = data.get('price')

    dsg = Product(name_of_product=name_of_goods, price=price)

    dsg.save()

    return JsonResponse(return_dict)



def management(request):
    print('Ololo xyi')
    return render(request, 'management/management.html')
