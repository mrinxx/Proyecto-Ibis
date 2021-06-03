from django.shortcuts import redirect, render
from django.http import JsonResponse #Se utiliza para mandar la respuesta en formato JSON
from django.core.serializers import serialize #Se usa para poder pasar QuerySet a Json
from .models import *
import datetime #utilizado para la validación de la fecha de nacimiento
from django.contrib.auth.models import User, Group
from .forms import LoginForm, RegisterForm
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth import decorators
from users.decorators import testGuardian

# Create your views here.

#Vista que muestra el formulario de inicio de sesión
def login(request):
    form=LoginForm()
    return render(request, "registration/login.html",{'form':form})      

#Vista para obtener el usuario que está registrandose cuando introduce su código de tutor
def guardianDetails(request):
    code = request.GET.get('code')
    guardian=Guardian.objects.filter(guardiancode=code)
    if guardian:
        userid=guardian[0].user_id
        user=User.objects.filter(id=userid)
        data={
            'guardian':serialize('json',guardian),
            'user':serialize('json',user)
        }
    else:
        data={
            'guardian':"",
            'user':""
        }
    return JsonResponse(data)

#Vista que realiza el "registro" de usuario en la BD
def register(request):
    # Peticion POST:
    #   -Se cogen los datos que podrían ser modificados por el usuario y se hace que se modifiquen en la base de datos
    #   -Se comprueban una serie de datos (checkboxes), si estos están en "on" significa que han sifdo marcados y por lo 
    #   tanto pasan a "si", ya que se guardan en la base de datos como "si" o "no" 
    #   -Se toma el usuario correspondiente al código de la BD y se modifica
    registerform=RegisterForm()
    if request.method=="POST":
        registerform=RegisterForm(data=request.POST)
        if registerform.is_valid():
            name=request.POST.get("name",'')
            lastname=request.POST.get("lastname",'')
            code=request.POST.get("code",'')
            dni=request.POST.get("dni")
            password=request.POST.get("password1",'')
            image=request.POST.get("userimage",'')
            phone=request.POST.get("phonenumber",'')
            email=request.POST.get("email",'')
            comunications=request.POST.get("comunications",'')
            viatype=request.POST.get("viatype",'')
            vianame=request.POST.get("vianame",'')
            vianumber=request.POST.get("vianumber",'') 
            floor=request.POST.get("floor",'')
            letter=request.POST.get("letter",'')
            cp=request.POST.get("cp",'')
            city=request.POST.get("city",'')
            try:
                guardian=Guardian.objects.filter(guardiancode=code); 
                guardian.update(image=image,dni=dni,phone=phone,privacity="si",terms="si",newsletter=comunications,via_type=viatype,via_name=vianame,via_number=vianumber,address_floor=floor,floor_letter=letter,cp=cp,city=city)
                
                user=User.objects.filter(id=guardian[0].user_id)[:1]
                #user[0].update(name=name,lastname=lastname,password=password,is_staff=False,is_active=True,email=email)
                user[0].name=name
                user[0].lastname=lastname
                user[0].set_password=password
                user[0].is_staff=False
                user[0].is_active=True #se activa el usuario para que pueda iniciar sesión
                user[0].is_superuser=False
                user[0].email=email
                # group = Group.objects.filter(name = "Guardians")                
                # user.groups.add(group) 
                return(redirect(reverse('login')+"?ok"))
            except:
                registerform=RegisterForm()
                return(redirect(reverse('register')+"?failure"))
    return render(request,"users/html/register.html",{'form':registerform})    


# # @method_decorator(testGuardian, name='dispatch')
@login_required(login_url="login") #en caso de no estar logueado, se redirige aqui
def guardianPanel(request):
    user=User.objects.filter(username=request.user)  #usuario logueado
    guardian=Guardian.objects.filter(user_id=user[0].id) #tutor legal que corresponde al usuario logueado
    children=Alumn.objects.filter(legal_tutor_id=guardian[0].guardiancode) #alumnos a cargo del tutor legal


    teachers=[] #se van a almacenar todos los profesores que los alumnos tengan (funcional cuando un tutor legal tirnr mas de un menor a su cargo)
    classrooms=[] #se van a almacenar las clases a las que pertenecen los menores a cargo del tutor legal
    userteachers=[]
    for child in children:
        classroom=Cicle.objects.filter(id=child.classroom_id) #se busca la clase en la que está el menor
        teacher=Teacher.objects.filter(id=classroom[0].teacher_id)
        teacheruser=User.objects.filter(id=teacher[0].user_id) #se busca el usuario correspondiente al tutor
        classrooms.append(classroom[0]) 
        userteachers.append(teacheruser[0])
        
    # teacher=Teacher.objects.filter(id=children.teacher_id)
    return render(request,'users/html/userpanel.html',{'user':user[0],'guardian':guardian[0],'children':children,'teachers':teachers,'userteacher':userteachers,'classrooms':classrooms})

# def validateDate(date):
#     today=datetime.datetime.now()
#     if date.getyear()>=  today.date.
