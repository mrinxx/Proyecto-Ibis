from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.
#Modelos que se van a  migrar a la base de datos y que sirven para formae los elementos de la web

class Event(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    Description=models.CharField(max_length=400)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


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




