from django.contrib import admin

from account.models import DatosEntrega

@admin.register(DatosEntrega)
class DatosEntregaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'direccion', 'codigo_postal', 'ciudad']

