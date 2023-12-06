from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
import random

# Un usuario puede tener múltiples reclamaciones
class Reclamacion(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    asunto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)
    STATUS_OPTIONS = [("EN", "Enviada"),
                        ("BR", "Bajo Revisión"),
                        ("RE", "Resuelta")]
    resolucion = models.CharField(max_length=250)
    estado_reclamacion = models.CharField(max_length=13, choices = STATUS_OPTIONS, default="EN")
    num_referencia = models.BigIntegerField(unique=True, default=0)
    def __str__(self):
        return f'Reclamacion {self.usuario}, {self.asunto}, {self.estado_reclamacion}'

    def save(self, *args, **kwargs):
            while True:
                nuevo_numero = random.randint(10**9, (10**10)-1)
                # Verificar si el número ya existe en la base de datos
                if not Reclamacion.objects.filter(num_referencia=nuevo_numero).exists():
                    break

            self.num_referencia = nuevo_numero
            super().save(*args, **kwargs)

# Una opinion tener múltiples combinaciones producto usuario
class Opinion(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ForeignKey(Product,on_delete=models.CASCADE)
    SCORE_OPTIONS = [(0,0),(0.5,0.5),(1,1),(1.5,1.5),
                      (2,2),(2.5,2.5),(3,3),(3.5,3.5),
                      (4,4),(4.5,4.5),(5,5)]
    puntuacion = models.DecimalField(max_digits=2, decimal_places=1, choices = SCORE_OPTIONS, default= 2.5)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f'Opinion {self.usuario}, {self.producto}, {self.puntuacion}'