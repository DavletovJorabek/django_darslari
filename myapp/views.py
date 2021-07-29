from django.shortcuts import render
from  django. http import HttpResponse
def hello (request):
    names = ['umid', 'sarvar', 'zafar']
    name = ''
    return render(request, 'index.html',{'ism':name, 'ismlar':names})


def goodbye(request):
    return HttpResponse("Xayr")


def ism(request):
    return HttpResponse('Assalomu aleykum Jorabek')
