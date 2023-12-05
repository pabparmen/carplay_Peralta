from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
import datetime
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

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
                field.many_to_many and not field.one_to_many]
    # Primera fila con la cabecera
    writer.writerow([field.verbose_name for field in fields])
    # Escribir las filas restatntes
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    export_to_csv.short_description = 'Export to CSV'

def pedido_detail(obj):
    url = reverse('pedidos:admin_pedido_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">Vista</a>')

def pedido_pdf(obj):
    url = reverse('pedidos:admin_pedido_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
    pedido_pdf.short_description = 'Recibo'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email',
    'direccion', 'codigo_postal', 'ciudad', 'opciones_envio', 'pagado',
    pedido_payment, 'creado', 'actualizado', 'coste_total','estado_pedido',
    'num_referencia', pedido_detail, pedido_pdf]
    list_filter = ['pagado', 'creado', 'actualizado', 'estado_pedido']
    inlines = [PedidoItemInline]
    actions = [export_to_csv]