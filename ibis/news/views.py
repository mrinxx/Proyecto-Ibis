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
    allimages=[getattr(mynew,"media2"),getattr(mynew,"media3"),getattr(mynew,"media4"),getattr(mynew,"media5"),getattr(mynew,"media6")] 
    images=[]
    for i in allimages:
        if(i==""):
            continue
        else:
            images.append(i)
    return render(request,"news/html/details.html",{'new':mynew,'images':images})

def firstNews(request):
    data = {
        'news' : serialize('json',New.objects.all()[:6]) # [:6] indica que solo se cojan los 6 primeros, los cuales se muestran en el index
    }
    return JsonResponse(data)