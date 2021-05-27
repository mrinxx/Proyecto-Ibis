from django.db import models

# Create your models here.

OPTIONS=[
     ("no", 'no'),
     ("si", 'si'),
]



class Guardian(models.Model):
    guardiancode=models.CharField(primary_key=True,max_length=10)
    guardianusername=models.CharField(max_length=9,unique=True,blank=False,null=False)
    password=models.CharField(max_length=20,default="",blank=False,null=False) #se va a almacenar por defecto una contraseña 
    dni=models.CharField(unique=True,max_length=9,blank=False,null=False)
    name=models.CharField(max_length=50,blank=False,null=False)
    last_name=models.CharField(max_length=150,blank=False,null=False)
    birth_date=models.DateField(blank=False,null=False)
    address=models.CharField(max_length=200,blank=False,null=False)
    city=models.CharField(max_length=50,blank=False,null=False)
    image=models.ImageField(upload_to="legal-guardian",blank=True,null=True)
    email=models.EmailField(blank=False,null=False)
    phone=models.CharField(max_length=9,blank=False,null=False)
    privacity=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)
    terms=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)
    newsletter=models.CharField(choices=OPTIONS,default="no",max_length=2,blank=True,null=True)
    activated=models.CharField(choices=OPTIONS,default="no",max_length=2)
    guardian_created_at=models.DateField(auto_now_add=True)
    guardian_updated_at=models.DateField(auto_now=True)

