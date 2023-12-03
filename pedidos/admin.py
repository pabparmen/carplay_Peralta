from django.contrib import admin

from .models import Pedido, PedidoItem

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    raw_id_fields = ['product']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email',
    'direccion', 'codigo_postal', 'ciudad', 'opciones_envio', 'pagado',
    'creado', 'actualizado', 'coste_total']
    list_filter = ['pagado', 'creado', 'actualizado']
    inlines = [PedidoItemInline]
