from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import Event,  Menu, Timetable, Resource
from news.models import New
from users.models import Teacher, Cicle
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    news = New.objects.all().order_by('-new_updated_at')[:6]
    return render(request, "core/html/index.html",{'news':news})

def about(request):
    users=User.objects.all()
    teachers=Teacher.objects.all()
    cicles=Cicle.objects.all()
    return render(request, "core/html/about.html",{'teachers':teachers,'users':users,'cicles':cicles})

def services(request):
    return render(request, "core/html/services.html")


def events(request):
    return render(request, "core/html/events.html",{'events':events})

def getEvents(request):
    data = {
        'events' : serialize('json',Event.objects.all().order_by('date')) 
    }
    return JsonResponse(data)

def firstEvents(request):
    data = {
        'events' : serialize('json',Event.objects.all()[:3]) # [:3] indica que solo se cojan los 3 primeros, los cuales se muestran en el index
    }
    return JsonResponse(data)


def getTimetables(request):
    timetables=Timetable.objects.all()
    cicles=[]
    for timetable in timetables:
        cicle=Cicle.objects.filter(id=timetable.cicle_id).first()
        cicles.append(cicle)
    data={
        'timetables' : serialize('json',timetables),
        'cicles':serialize('json',cicles)
    }
    return JsonResponse(data)

def getMenus(request):
    data={
        'menus' : serialize('json',Menu.objects.all())
    }
    return JsonResponse(data)

def search(request):
    tosearch=request.GET["toSearch"]+"%"
    news=New.objects.raw("SELECT * FROM news where title like %s",[tosearch]) 
    events=Event.objects.raw("SELECT * FROM events where Description like %s",[tosearch]) 
    resources=Resource.objects.raw("SELECT * FROM resources where description like %s",[tosearch]) 
    data={
        'news' : serialize('json',news),
        'events' : serialize('json',events),
        'resources' : serialize('json',resources)
    }
    return JsonResponse(data)
    


# def getResources(request):
#     data={
#         'menus' : serialize('json',Menu.objects.all())
#     }
#     return JsonResponse(data)