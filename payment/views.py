from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from pedidos.models import Pedido

# creación de la instancia Stripe 
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    pedido_id = request.session.get('pedido_id',None)
    pedido=get_object_or_404(Pedido, id=pedido_id)

    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

        #Stripe checkout session data
        session_data={
            'mode': 'payment',
            'client_reference_id': pedido.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # add pedido items to the Stripe checkout session
        for item in pedido.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        #redirect to Stripe payment form
        return redirect(session.url,code=303)
    else:
        return render(request,'payment/process.html',locals())

def payment_completed(request):
    pedido_id = request.session.get('pedido_id',None)
    pedido=get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'payment/completed.html', {'pedido':pedido})

def payment_canceled(request):
 return render(request, 'payment/canceled.html')
