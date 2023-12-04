import random
from django.db import models
from shop.models import Product

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    SHIPMENT_OPTIONS = [("GE", "General"),
                        ("EX", "Express"),
                        ("RT", "Recogida en Tienda")]
    opciones_envio =models.CharField(max_length=18, choices = SHIPMENT_OPTIONS, default="GE")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)
    coste_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    STATUS_OPTIONS = [("EP", "En preparación"),
                        ("EC", "En camino"),
                        ("RB", "Recibido")]
    estado_pedido =models.CharField(max_length=14, choices = STATUS_OPTIONS, default="EP")

    num_referencia = models.BigIntegerField(unique=True, default=0)

    def save(self, *args, **kwargs):
        while True:
            nuevo_numero = random.randint(10**9, (10**10)-1)
            # Verificar si el número ya existe en la base de datos
            if not Pedido.objects.filter(num_referencia=nuevo_numero).exists():
                break

        self.num_referencia = nuevo_numero
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-creado']
        indexes = [
        models.Index(fields=['-creado']),
        ]

    def __str__(self):
        return f'Pedido {self.id}'
    
    def get_total_cost(self):
        coste_total_sin_envio = sum(item.get_cost() for item in self.items.all())
        #El coste del envio general si el pedido excede los 50 se reduce a 0
        #sino es 10 y si es express 20
        if self.opciones_envio == "GE" and coste_total_sin_envio < 50:
            self.coste_total = coste_total_sin_envio + 10
            self.save()
            return coste_total_sin_envio + 10
        elif self.opciones_envio == "EX":
            self.coste_total = coste_total_sin_envio + 20
            self.save()
            return coste_total_sin_envio + 20
        else:
            self.coste_total = coste_total_sin_envio
            self.save()
            return coste_total_sin_envio

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido,
    related_name='items',
    on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
    related_name='pedido_items',
    on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
    decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity

