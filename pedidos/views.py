from django.shortcuts import render
from .models import PedidoItem, Pedido
from .forms import PedidoCreateForm
from cart.cart import Cart

def pedido_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = PedidoCreateForm(request.POST)
        if form.is_valid():
            pedido = form.save()
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
