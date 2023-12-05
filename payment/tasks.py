from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from carplay_Peralta import settings
from pedidos.models import Pedido
from io import BytesIO
from celery import shared_task
import weasyprint

@shared_task
def payment_completed(pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    # Creamos el email de recibo
    subject = f'Carplay Peralta - Recibo no. {pedido.num_referencia}'
    message = 'Porfavor, he aquí su recibo de su reciente compra.'
    email = EmailMessage(subject,
                        message,
                        'admin@carplayperalta.com',
                        [pedido.email])
    # Genearmos el PDF
    html = render_to_string('pedidos/pedido/pdf.html', {'pedido': pedido})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                    stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'pedido_{pedido.id}.pdf',
                    out.getvalue(),
                    'application/pdf')
    # Mandamos el e-mail
    email.send()