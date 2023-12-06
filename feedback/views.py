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
            return render(request, 'feedback/reclamacion/reclamacion_enviada.html', {'user': request.user})
    else:
        form = UserReclamacionForm()

    return render(request, 'feedback/reclamacion/form_reclamacion.html', {'user': request.user, 'form': form})
@login_required
def list_reclamaciones(request):
    reclamaciones = Reclamacion.objects.filter(usuario=request.user)
    return render(request, 'feedback/reclamacion/lista_reclamaciones.html', {'reclamaciones': reclamaciones})
