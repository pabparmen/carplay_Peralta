from django import forms
from django.contrib.auth.models import User
from .models import Reclamacion, Opinion
from shop.models import Product

class UserReclamacionForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['asunto', 'descripcion']

class UserOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['puntuacion', 'descripcion']