from django.db import models
from django.contrib.auth.models import User

# Create your models here.

OPTIONS=[
     ("no", 'no'),
     ("si", 'si'),
]

VIA_TYPES=[
     ("CL","Calle"),
     ("AV","Avenida"),
     ("CJ","Callejón"),
     ("BL","Bulevar"),
     ("CA","Camino")
]

AGE_CLASS= [
        ("1E", '0-1 años'),
        ("2E", '1-2 años'),
        ("3E", '2-3 años'),
        ("4E", '3-4 años'),
        ("5E", '4-5 años'),
        ("6E", '5-6 años'),
    ]

class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guardiancode=models.CharField(primary_key=True,max_length=10)
    password=models.CharField(max_length=20,default="",blank=False,null=False) #se va a almacenar por defecto una contraseña 
    dni=models.CharField(unique=True,max_length=9,blank=False,null=False)
    birth_date=models.DateField(blank=False,null=False)
    via_type=models.CharField(choices=VIA_TYPES,default="CL",max_length=2,blank=False,null=False)
    via_name=models.CharField(max_length=100,blank=False,null=False)
    via_number=models.IntegerField(default=0,blank=False,null=False) #0 significará que es s/n
    address_floor=models.IntegerField(blank=False,null=False)
    floor_letter=models.CharField(max_length=9,default="",blank=False,null=False)
    cp=models.IntegerField(blank=False,null=False)
    city=models.CharField(max_length=50,blank=False,null=False)
    image=models.ImageField(upload_to="legal-guardian",blank=True,null=True)
    phone=models.CharField(max_length=9,blank=False,null=False)
    privacity=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)
    terms=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)
    newsletter=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)


# ?????????????????????????????????? TODO: necesario???
class People(models.Model):
    KIND_OF_JOBS= [
        ("DR", 'Directiva'),
        ("TC", 'Profesorado'),
        ("PS", 'Psicología'),
        ("AS", 'Ayuda Sanitaria'),
        ("AI", 'Asistencia al infante'),
        ("TC", 'Técnico especialista'),
        ("PA", "PAS"),
]
    id=models.AutoField(primary_key=True)
    dni=models.CharField(unique=True,max_length=9)
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)
    birth_date=models.DateField()
    job=models.CharField(choices=KIND_OF_JOBS,default="TC",max_length=2)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    image=models.ImageField(upload_to="people")
   

class Teacher(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     id=models.AutoField(primary_key=True)
     dni=models.CharField(unique=True,max_length=9)
     birth_date=models.DateField()
     via_type=models.CharField(choices=VIA_TYPES,default="CL",max_length=2,blank=False,null=False)
     via_name=models.CharField(max_length=100,blank=False,null=False)
     via_number=models.IntegerField(default=0,blank=False,null=False) #0 significará que es s/n
     address_floor=models.IntegerField(blank=False,null=False)
     floor_letter=models.CharField(max_length=9,default="",blank=False,null=False)
     cp=models.IntegerField(blank=False,null=False)
     city=models.CharField(max_length=50,blank=False,null=False)
     image=models.ImageField(upload_to="teachers",blank=True,null=True)
    

class Alumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    dni=models.CharField(unique=True,max_length=9)
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)
    birth_date=models.DateField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    image=models.ImageField(upload_to="alumns",blank=True)
    classroom=models.CharField(choices=AGE_CLASS,default="1E",max_length=2)
    legal_tutor=models.ForeignKey(Guardian, on_delete=models.CASCADE) #1 alumno 1 tutor legal -> 1 tutor legal muchos alumnos
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) #1 alumno 1 tutor -> 1 tutto muchos alumnos
   

