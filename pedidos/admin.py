from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Pedido, PedidoItem

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    raw_id_fields = ['product']

def pedido_payment(obj):
    url=obj.get_stripe_url()
    if obj.stripe_id:
        html= f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
pedido_payment.short_description = 'Stripe payment'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email',
    'direccion', 'codigo_postal', 'ciudad', 'opciones_envio', 'pagado',
    'creado', 'actualizado', 'coste_total','estado_pedido', 'num_referencia', pedido_payment]
    list_filter = ['pagado', 'creado', 'actualizado', 'estado_pedido']
    inlines = [PedidoItemInline]
