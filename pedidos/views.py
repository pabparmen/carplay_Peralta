from django.urls import reverse
from django.shortcuts import render, redirect
from .models import PedidoItem
from .forms import PedidoCreateForm
from cart.cart import Cart
from pedidos.models import Pedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def pedido_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = PedidoCreateForm(request.POST)
        
        if form.is_valid():
            pedido = form.save(commit=False)
            coste = float(cart.get_total_price())
            pedido.user = request.user
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

# @login_required
# def estado_pedidos(request):
#     # Obtener los pedidos asociados al usuario actual
#     pedidos = Pedido.objects.filter(user=request.user)

#     # Puedes agregar más lógica según tus necesidades

#     return render(request, 'estado_pedidos.html', {'estado_pedidos': estado_pedidos})
