from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import Event, Guardian, Menu, Timetable


# Create your views here.
def home(request):
    return render(request, "core/html/index.html")

def about(request):
    return render(request, "core/html/about.html")

def services(request):
    return render(request, "core/html/services.html")

def contact(request):
    return render(request, "core/html/contact.html") 

#TODO: Cambio
def users(request):
    return render(request, "core/html/login.html")       


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


def guardianDetails(request):
    code = request.GET.get('code')
    data={
        'guardian':serialize('json',Guardian.objects.filter(guardiancode=code))
    }
    return JsonResponse(data)
    
def register(request):
    # Peticion POST:
    #   -Se cogen los datos que podrían ser modificados por el usuario y se hace que se modifiquen en la base de datos
    #   -Se comprueban una serie de datos (checkboxes), si estos están en "on" significa que han sifdo marcados y por lo 
    #   tanto pasan a "si", ya que se guardan en la base de datos como "si" o "no" 
    #   -Se toma el usuario correspondiente al código de la BD y se modifica
    if request.method=="POST":
        code=request.POST["usercode"]
        image=request.POST["userimage"]
        phone=request.POST["phonenumber"]
        email=request.POST["email"]
        address=request.POST["address"]
        privpolicy=request.POST["privacitypolicy"]
        comunications=request.POST["comunications"]
        terms=request.POST["terms"]

        if(privpolicy=="on"):
            privpolicy="si"
        else:
            privpolicy="no"
        
        if(terms=="on"):
            terms="si"
        else:
            terms="no"
        #PROBLEMA
        if(comunications=="on"):
            comunications="si"
        else:
           comunications="no"
        
        Guardian.objects.filter(guardiancode=code).update(image=image,phone=phone,email=email,address=address,activated="si",privacity=privpolicy,terms=terms,newsletter=comunications)
        return render(request, "core/html/register.html") 
    return render(request,"core/html/register.html")

# def getResources(request):
#     data={
#         'menus' : serialize('json',Menu.objects.all())
#     }
#     return JsonResponse(data)