from django.db import models

# Create your models here.
#Modelos que se vana  migrar a la base de datos y que sirven para formae los elementos de la web

class New(models.Model):
    new_id=models.AutoField(primary_key=True) #Id autoincremental
    new_title=models.CharField(max_length=100)
    new_subtitle=models.CharField(max_length=50)
    new_content=models.CharField(max_length=1400)
    new_media1=models.ImageField(upload_to="news/")
    #Estas imágenes no son obligatorias, solo lo es una para el encabezado de la noticia
    new_media2=models.ImageField(blank=True)
    new_media3=models.ImageField(blank=True)
    new_media4=models.ImageField(blank=True)
    new_media5=models.ImageField(blank=True)
    new_media6=models.ImageField(blank=True)
    new_created_at=models.DateField(auto_now_add=True)
    new_updated_at=models.DateField(auto_now=True)

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_date=models.DateField()
    event_Description=models.CharField(max_length=400)
    event_created_at=models.DateField(auto_now_add=True)
    event_updated_at=models.DateField(auto_now=True)