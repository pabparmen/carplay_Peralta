from django.contrib import admin
from .models import Reclamacion, Opinion

@admin.register(Reclamacion)
class ReclamacionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'asunto', 'descripcion', 'estado_reclamacion']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'producto', 'puntuacion', 'descripcion']
