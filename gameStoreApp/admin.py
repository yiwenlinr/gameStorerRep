from django.contrib import admin
from gameStoreApp.models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','cargo','email','telefono','direccion']
# Register your models here.
admin.site.register(Proyecto)

