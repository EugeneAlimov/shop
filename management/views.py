from django.shortcuts import render


# Create your views here.
def management(request):
    print('Ololo xyi')
    return render(request, 'management/management.html')
