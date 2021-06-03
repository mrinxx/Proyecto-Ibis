from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import django.utils.timezone
# Create your models here.

OPTIONS=[
     ("no", 'no'),
     ("si", 'si'),
]

VIA_TYPES=[
     ("Calle","Calle"),
     ("Avenida","Avenida"),
     ("Callejón","Callejón"),
     ("Bulevar","Bulevar"),
     ("Camino","Camino")
]

AGE_CLASS= [
        ("0-1 años", '0-1 años'),
        ("1-2 años", '1-2 años'),
        ("2-3 años", '2-3 años'),
        ("3-4 años", '3-4 años'),
        ("4-5 años", '4-5 años'),
        ("5-6 años", '5-6 años'),
    ]


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    guardiancode=models.CharField(primary_key=True,max_length=10)
    dni=models.CharField(unique=True,max_length=9,blank=False,null=False)
    birth_date=models.DateField(default=django.utils.timezone.now,blank=False,null=False)
    via_type=models.CharField(choices=VIA_TYPES,default="Calle",max_length=8,blank=False,null=False)
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

class Teacher(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
     id=models.AutoField(primary_key=True)
     dni=models.CharField(unique=True,max_length=9)
     birth_date=models.DateField(default=django.utils.timezone.now,blank=False,null=False)
     via_type=models.CharField(choices=VIA_TYPES,default="Calle",max_length=8,blank=False,null=False)
     via_name=models.CharField(max_length=100,blank=False,null=False)
     via_number=models.IntegerField(default=0,blank=False,null=False) #0 significará que es s/n
     address_floor=models.IntegerField(blank=False,null=False)
     floor_letter=models.CharField(max_length=9,default="",blank=False,null=False)
     cp=models.IntegerField(blank=False,null=False)
     city=models.CharField(max_length=50,blank=False,null=False)
     image=models.ImageField(upload_to="teachers",blank=True,null=True)
 
class Cicle(models.Model):
    id=models.AutoField(primary_key=True)
    classroom=models.CharField(choices=AGE_CLASS,default="0-1 años",max_length=8,unique=True)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)#una clase solo puede tener un tutor
class Alumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    id=models.AutoField(primary_key=True)
    dni=models.CharField(unique=True,max_length=9)
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)
    birth_date=models.DateField(default=django.utils.timezone.now,blank=False,null=False)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    image=models.ImageField(upload_to="alumns",blank=True)
    legal_tutor=models.ForeignKey(Guardian, on_delete=models.CASCADE) #1 alumno 1 tutor legal -> 1 tutor legal muchos alumnos
    classroom = models.ForeignKey(Cicle, on_delete=models.CASCADE) #1 alumno 1 tutor -> 1 tutto muchos alumnos
   

