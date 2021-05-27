from django.db import models
from users.models import Guardian
# Create your models here.
#Modelos que se vana  migrar a la base de datos y que sirven para formae los elementos de la web



class Event(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    Description=models.CharField(max_length=400)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

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
    teacher_created_at=models.DateField(auto_now_add=True)
    teacher_updated_at=models.DateField(auto_now=True)

AGE_CLASS= [
        ("1E", '0-1 años'),
        ("2E", '1-2 años'),
        ("3E", '2-3 años'),
        ("4E", '3-4 años'),
        ("5E", '4-5 años'),
        ("6E", '5-6 años'),
    ]
class Timetable(models.Model):
    id=models.AutoField(primary_key=True)
    age=models.CharField(choices=AGE_CLASS,default="1E",max_length=2)
    timetable_image=models.ImageField(upload_to="timetables")
    timetable_created_at=models.DateField(auto_now_add=True)
    timetable_updated_at=models.DateField(auto_now=True)

class Menu(models.Model):
    id=models.AutoField(primary_key=True)
    age=models.CharField(choices=AGE_CLASS,default="1E",max_length=2)
    menu_image=models.ImageField(upload_to="menus")
    menu_created_at=models.DateField(auto_now_add=True)
    menu_updated_at=models.DateField(auto_now=True)

OPTIONS=[
     ("no", 'no'),
     ("si", 'si'),
]


class Alumn(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(unique=True,max_length=9)
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)
    birth_date=models.DateField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    image=models.ImageField(upload_to="alumns",blank=True)
    classroom=models.CharField(choices=AGE_CLASS,default="1E",max_length=2)
    legal_tutor=models.ForeignKey(Guardian, on_delete=models.CASCADE)
    alumn_created_at=models.DateField(auto_now_add=True)
    alumn_updated_at=models.DateField(auto_now=True)