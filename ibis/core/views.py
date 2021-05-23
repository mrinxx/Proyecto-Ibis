from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import Event, Menu, Timetable
from .models import New


# Create your views here.
def home(request):
    return render(request, "core/html/index.html")

def about(request):
    return render(request, "core/html/about.html")

def services(request):
    return render(request, "core/html/services.html")

def contact(request):
    return render(request, "core/html/contact.html") 

def news(request):
    return render(request,"core/html/news.html")
    
def register(request):
    return render(request,"core/html/register.html")

#TODO: Cambio
def users(request):
    return render(request, "core/html/login.html")       

def newDetails(request,newtitle):
    return render(request,newtitle,"core/html/new-detail.html")

def firstEvents(request):
    data = {
        'events' : serialize('json',Event.objects.all()[:3]) # [:3] indica que solo se cojan los 3 primeros, los cuales se muestran en el index
    }
    return JsonResponse(data)

def firstNews(request):
    data = {
        'news' : serialize('json',New.objects.all()[:6]) # [:6] indica que solo se cojan los 6 primeros, los cuales se muestran en el index
    }
    return JsonResponse(data)


def getNews(request):
    data = {
        'news' : serialize('json',New.objects.all())
    }
    return JsonResponse(data)

def getEvents(request):
    data = {
        'events' : serialize('json',Event.objects.all().order_by('date')) 
    }
    return JsonResponse(data)

def getTimetables(request):
    data={
        'timetables' : serialize('json',Timetable.objects.all())
    }
    return JsonResponse(data)

def getMenus(request):
    data={
        'menus' : serialize('json',Menu.objects.all())
    }
    return JsonResponse(data)

# def getResources(request):
#     data={
#         'menus' : serialize('json',Menu.objects.all())
#     }
#     return JsonResponse(data)