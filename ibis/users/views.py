from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import *
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        guardian=Guardian.objects.filter(guardianusername=username).filter(password=password)
        if guardian:
            return redirect(guardianPanel,username)
        else:
            return render(request, "users/html/login.html")    
    return render(request, "users/html/login.html")      

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
        password=request.POST["password"]
        image=request.POST["userimage"]
        phone=request.POST["phonenumber"]
        email=request.POST["email"]
        address=request.POST["address"]
        comunications=request.POST["comunications"]    
        Guardian.objects.filter(guardiancode=code).update(password=password,image=image,phone=phone,email=email,address=address,activated="si",privacity="si",terms="si",newsletter=comunications)
        return redirect(login)
    return render(request,"users/html/register.html")    

def guardianPanel(request,username):
    guardian=Guardian.objects.filter(guardianusername=username)
    return render(request,'users/html/userpanel.html',{'user':guardian})