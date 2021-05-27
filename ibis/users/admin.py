from django.contrib import admin
from .models import Guardian

class readOnly(admin.ModelAdmin):
    readonly_fields=('guardian_created_at','guardian_updated_at')
# Register your models here.
admin.site.register(Guardian,readOnly)