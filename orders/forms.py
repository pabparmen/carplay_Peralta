from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellidos', 'email',
                'direccion','codigo_postal', 'ciudad', 'opciones_envio']