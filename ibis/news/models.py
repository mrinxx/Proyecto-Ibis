from django.db import models

# Create your models here.
class New(models.Model):
    id=models.AutoField(primary_key=True) #Id autoincremental
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    content=models.CharField(max_length=1400)
    media1=models.ImageField(upload_to="news")
    #Estas imágenes no son obligatorias, solo lo es una para el encabezado de la noticia
    media2=models.ImageField(blank=True)
    media3=models.ImageField(blank=True)
    media4=models.ImageField(blank=True)
    media5=models.ImageField(blank=True)
    media6=models.ImageField(blank=True)
    new_created_at=models.DateField(auto_now_add=True)
    new_updated_at=models.DateField(auto_now=True)