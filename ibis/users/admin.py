from django.contrib import admin
from .models import Guardian
from django.contrib.auth.models import User
class readOnly(admin.ModelAdmin):
    readonly_fields=('guardian_created_at','guardian_updated_at',"privacity","terms","newsletter","activated")
# Register your models here.
admin.site.register(Guardian,readOnly)