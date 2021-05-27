from django.contrib import admin
from .models import New

#Estos datos solo van a poder leerse en el admin
class readOnly(admin.ModelAdmin):
    readonly_fields=('new_created_at','new_updated_at')

# Register your models here.
admin.site.register(New,readOnly)