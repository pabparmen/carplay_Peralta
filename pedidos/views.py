from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
import weasyprint
from .models import PedidoItem, Pedido
from .forms import PedidoCreateForm
from cart.cart import Cart
from carplay_Peralta import settings

def pedido_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = PedidoCreateForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            coste = float(cart.get_total_price())
            if pedido.opciones_envio == "GE" and coste < 50:
                pedido.coste_total = coste + 10
            elif pedido.opciones_envio == "EX":
                pedido.coste_total = coste + 20
            else:
                pedido.coste_total = coste
                pedido.save()
            pedido.save()
            for item in cart:
                PedidoItem.objects.create(pedido=pedido,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'])
                
            #Clear the cart
            cart.clear()

            #set the pedido in the session
            request.session['pedido_id']=pedido.id
            #redirección a payment
            return redirect(reverse('payment:process'))
        
    else:
        form = PedidoCreateForm()
    return render(request,
        'pedidos/pedido/create.html',
        {'cart': cart, 'form': form})

@staff_member_required
def admin_pedido_detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request,
    'admin/pedidos/pedido/detail.html',
    {'pedido': pedido})

@staff_member_required
def admin_pedido_pdf(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    html = render_to_string('pedidos/pedido/pdf.html',
                            {'pedido': pedido})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=pedido_{pedido.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT / 'css/pdf.css')])
    return response