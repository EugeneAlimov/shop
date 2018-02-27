from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from management.forms import *
from products.models import *
from django.views import View

# Create your views here.

# class FileFieldView(FormView):
#     form_class = UploadImageForm
#     template_name = 'management.html'  # Replace with your template.
#     success_url = 'goods/goods_adding'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         print('form')
#         if form.is_valid():
#             for f in files:
#
#                 form.save()# Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def goods_adding(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        print('Есть форма')
        form.save()
    else:
        print('Пусто')

    # return_dict = dict()
    data = request.POST
    print(data)

    data = request.POST
    print('Добавление товара')
    name_of_goods = data.get('name_of_goods')
    price = data.get('price')
    goods_description = data.get('goods_description')
    goods_short_description = data.get('goods_short_description')
    choice_category = data.get('category')
    currency = data.get('currency')
    quantity = data.get('quantity')
    dsg = Product(name_of_product=name_of_goods, price=price, short_description=goods_short_description,
                  description=goods_description, category=choice_category, currency=currency, quantity=quantity)

    dsg.save()
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
