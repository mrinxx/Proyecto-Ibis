from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import Event,  Menu, Timetable
from news.models import New
from users.models import Teacher, Cicle
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    news=New.objects.all()[:6]
    return render(request, "core/html/index.html",{'news':news})

def about(request):
    users=User.objects.all()
    teachers=Teacher.objects.all()
    cicles=Cicle.objects.all()
    return render(request, "core/html/about.html",{'teachers':teachers,'users':users,'cicles':cicles})

def services(request):
    return render(request, "core/html/services.html")




def firstEvents(request):
    data = {
        'events' : serialize('json',Event.objects.all()[:3]) # [:3] indica que solo se cojan los 3 primeros, los cuales se muestran en el index
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