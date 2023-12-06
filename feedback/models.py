from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Un usuario puede tener múltiples reclamaciones
class Reclamacion(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    asunto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)
    STATUS_OPTIONS = [("EN", "Enviada"),
                        ("BR", "Bajo Revisión"),
                        ("RE", "Resuelta")]
    estado_reclamacion = models.CharField(max_length=13, choices = STATUS_OPTIONS, default="EN")

    def __str__(self):
        return f'Reclamacion {self.usuario}, {self.asunto}, {self.estado_reclamacion}'

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