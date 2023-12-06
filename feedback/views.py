from django.shortcuts import render
from django.http import HttpResponse
from .models import Reclamacion, Opinion 
from django.contrib.auth import authenticate, login 
from .forms import UserReclamacionForm, UserOpinionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def form_reclamacion(request):
    if request.method == 'POST':
        form = UserReclamacionForm(request.POST)
        if form.is_valid():
            reclamacion = form.save(commit=False)
            reclamacion.usuario = request.user
            reclamacion.save()
            return render(request, 'feedback/reclamacion/list.html', {'user': request.user})
    else:
        form = UserReclamacionForm(instance=reclamacion)

    return render(request, 'feedback/reclamacion/form_reclamacion.html', {'user': request.user, 'form': form})

@login_required
def form_opinion(request):
    try:
        opinion = Opinion.objects.filter(usuario=request.user).filter(producto=request.product).get()
    except Opinion.DoesNotExist:
        opinion = None 
    
    if request.method == 'POST':
        if opinion: #si existen datos se actualiza el formulario
            form = UserOpinionForm(request.POST, instance=opinion)
        else:  # Si no existen datos de entrega crea un nuevo formulario
            form = UserOpinionForm(request.POST)

        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.usuario = request.user
            opinion.producto = request.product
            opinion.save()
            #Debe volver al detalle del producto del cual se crea opinion
            return render(request, 'feedback/profile.html', {'user': request.user, 'opinion':opinion})
    else:
        form = UserOpinionForm(instance=opinion)

    return render(request, 'feedback/form_opinion.html', {'user': request.user, 'form': form})