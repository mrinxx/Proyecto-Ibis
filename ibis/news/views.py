from django.shortcuts import render
from .models import *
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json

def news(request):
    return render(request,"news/html/news.html")

# Create your views here.
def getNews(request):
    data = {
        'news' : serialize('json',New.objects.all())
    }
    return JsonResponse(data)

def details(request,id):
    mynew=New.objects.filter(id=id)
    return render(request,"news/html/details.html",{'new':mynew})

