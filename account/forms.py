from django import forms
from django.contrib.auth.models import User
from .models import DatosEntrega

class LoginForm(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    contraseña = forms.CharField(label='Contraseña' , widget=forms.PasswordInput )
    contraseña2 = forms.CharField(label='Repite la contraseña' , widget=forms.PasswordInput )


    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
             'email': 'Correo electrónico',
           
        }

    def clean_contrasena2(self):
        cd = self.cleaned_data
        if cd['contraseña'] != cd['contraseña2']:
            raise forms.ValidationError('La contraseña no coincide')
        return cd['contraseña2']


class UserDatosEntregaForm(forms.ModelForm):
    class Meta:
        model = DatosEntrega
        fields = ['direccion', 'codigo_postal', 'ciudad']
    
class BusquedaPedidoForm(forms.Form):
    num_referencia = forms.IntegerField(label='Número de referencia')

