import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from payment.tasks import payment_completed
from pedidos.models import Pedido


@csrf_exempt
def stripe_webhook(request):
   payload = request.body
   sig_header = request.META['HTTP_STRIPE_SIGNATURE']
   event = None
   try:
     event = stripe.Webhook.construct_event(
       payload,
       sig_header,
       settings.STRIPE_WEBHOOK_SECRET)
   except ValueError as e:
     # Invalid payload

     return HttpResponse(status=400)
   except stripe.error.SignatureVerificationError as e:
     # Invalid signature
     return HttpResponse(status=400)
   
   if event.type =='checkout.session.completed':
     session = event.data.object
     if session.mode == 'payment' and session.payment_status == 'paid':
       try:
         pedido = Pedido.objects.get(id=session.client_reference_id)
       except Pedido.DoesNotExist:
         return HttpResponse(status=404)
       #marca las ordenes como pagadas
       pedido.pagado = True
       #almacena el Stripe ID del pago
       pedido.stripe_id=session.payment_intent
       pedido.save()
       # launch asynchronous task
       print('print 1')
       payment_completed.delay(pedido.id)
   return HttpResponse(status=200)