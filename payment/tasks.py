from django.core.mail import EmailMessage
from pedidos.models import Pedido, PedidoItem
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def payment_completed(pedido_id):
    
    pedido = Pedido.objects.get(id=pedido_id)

    subject = f'Carplay Peralta - Confirmacion de pedido #{pedido.num_referencia}'

    message = f'Gracias por comprar con Carplay Peralta, {pedido.nombre} {pedido.apellidos}!\n\n'
    message += f'Detalles de tu pedido:\n\n'

    #Detalles del Cliente
    message += f'El codigo de referencia es: #{pedido.num_referencia} \n'
    message += f'Direccion de envio:\n'
    message += f'Dirección: {pedido.direccion}\n'
    message += f'Codigo postal:{pedido.codigo_postal}\n'
    message += f'Ciudad: {pedido.ciudad}\n\n'


    #Detalles de la compra
    for item in pedido.items.all():
        message += f'Producto: {item.product.name}\n'
        message += f'Cantidad: {item.quantity}\n'
        message += f'Precio ud.: ${item.price}\n'
        message += f'Precio total: ${item.get_cost()}\n\n'

    message += f'Coste total: ${pedido.coste_total}\n\n'

    message += 'Esperamos volver a verle.'

    # email = EmailMessage(
    #     subject,
    #     message,
    #     'peraltacarplay@gmail.com',
    #     [pedido.email])

    # email.send()

    from_email = settings.EMAIL_HOST_USER
    to_email = pedido.email
    print('Pasa por aqui: ', to_email)

    send_mail(subject, message, from_email, [to_email])