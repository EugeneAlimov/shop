from django.http import JsonResponse, HttpResponse
from products.models import *


# Create your views here.
def goods_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print('Ololo')
    print(request.POST)
    data = request.POST

    return JsonResponse(return_dict)


def item(request):
    if request.method == 'POST':
        print('dfg')
        return HttpResponse('200')
