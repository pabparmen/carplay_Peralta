from django.shortcuts import render
from django.http import HttpResponse
from account.models import DatosEntrega 
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, BusquedaPedidoForm
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                usuario=cd['usuario'],
                                contraseña=cd['contraseña'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autentificación correcta')
                else:
                    return HttpResponse('Cuenta desactivada')
            else:
                return HttpResponse('Inicio de sesión inválido')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['contraseña'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'user_form': user_form})

def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def datos(request):
    return render(request, 'account/datos.html', {'section': 'datos'})

@login_required
def view_profile(request):

    datos_entrega = DatosEntrega.objects.all().filter(usuario = request.user).get()
    return render(request, 'account/profile.html', {'user': request.user, 'datos_entrega':datos_entrega})



def buscar_pedido_por_id(request):
    resultados = None
    form = BusquedaPedidoForm()  # Por defecto, muestra el formulario vacío
    
    if request.method == 'POST':
        form = BusquedaPedidoForm(request.POST)
        if form.is_valid():
            id_pedido = form.cleaned_data['id_pedido']
            resultados = Pedido.objects.filter(id=id_pedido)
    
    return render(request, 'account/dashboard.html', {'form': form, 'resultados': resultados})
