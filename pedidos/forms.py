from django import forms
from .models import Pedido
class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellidos', 'email',
                'direccion','codigo_postal', 'ciudad', 'opciones_envio']