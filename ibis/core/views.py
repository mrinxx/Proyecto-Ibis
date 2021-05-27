from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import Event,  Menu, Timetable


# Create your views here.
def home(request):
    return render(request, "core/html/index.html")

def about(request):
    return render(request, "core/html/about.html")

def services(request):
    return render(request, "core/html/services.html")

def contact(request):
    return render(request, "core/html/contact.html") 


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