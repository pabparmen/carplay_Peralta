from django.shortcuts import render
from .models import PedidoItem
from .forms import PedidoCreateForm
from cart.cart import Cart

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
        return render(request,
            'pedidos/pedido/created.html',
            {'pedido': pedido})
    else:
        form = PedidoCreateForm()
    return render(request,
        'pedidos/pedido/create.html',
        {'cart': cart, 'form': form})
