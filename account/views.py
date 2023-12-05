from django.shortcuts import render
from django.http import HttpResponse
from account.models import DatosEntrega 
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, BusquedaPedidoForm, UserDatosEntregaForm
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

def reclamaciones(request):
    return render(request, 'account/reclamaciones.html', {'section': 'reclamaciones'})

def terminos_de_uso_y_privacidad(request):
    return render(request, 'account/terminos_de_uso_y_privacidad.html', {'section': 'terminos_de_uso_y_privacidad'})



@login_required
def view_profile(request):
    try:
        datos_entrega = DatosEntrega.objects.all().filter(usuario = request.user).get()
        return render(request, 'account/profile.html', {'user': request.user, 'datos_entrega':datos_entrega})

    except DatosEntrega.DoesNotExist:
        return render(request, 'account/profile.html', {'user': request.user})


def buscar_pedido_por_id(request):
    resultados = None
    form = BusquedaPedidoForm()  # Por defecto, muestra el formulario vacío
    
    if request.method == 'POST':
        form = BusquedaPedidoForm(request.POST)
        if form.is_valid():
            num_referencia = form.cleaned_data['num_referencia']
            resultados = Pedido.objects.filter(num_referencia=num_referencia)
    
    return render(request, 'account/dashboard.html', {'form': form, 'resultados': resultados})

@login_required
def form_datos_entrega(request):
    try:
        datos_entrega = DatosEntrega.objects.get(usuario=request.user)
    except DatosEntrega.DoesNotExist:
        datos_entrega = None
       
    
    if request.method == 'POST':
        if datos_entrega: #si existen datos se actualiza el formulario
            form = UserDatosEntregaForm(request.POST, instance=datos_entrega)
        else:  # Si no existen datos de entrega crea un nuevo formulario
            form = UserDatosEntregaForm(request.POST)

        if form.is_valid():
            datos_entrega = form.save(commit=False)
            datos_entrega.usuario = request.user
            datos_entrega.save()
            return render(request, 'account/profile.html', {'user': request.user, 'datos_entrega':datos_entrega})
    else:
        form = UserDatosEntregaForm(instance=datos_entrega)

    return render(request, 'account/form_datos_entrega.html', {'user': request.user, 'form': form})

@login_required
def estado_pedidos(request):
    # Obtener los pedidos asociados al usuario actual
    pedidos = Pedido.objects.filter(user=request.user)

    # Puedes agregar más lógica según tus necesidades

    return render(request, 'account/estado_pedidos.html', {'pedidos': pedidos})