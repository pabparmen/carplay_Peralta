from django.db import models
from django.contrib.auth.models import User

class DatosEntrega(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f'DatosEntrega {self.usuario}, {self.direccion}'