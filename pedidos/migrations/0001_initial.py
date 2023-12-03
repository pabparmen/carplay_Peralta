# Generated by Django 4.1.13 on 2023-12-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("direccion", models.CharField(max_length=250)),
                ("codigo_postal", models.CharField(max_length=20)),
                ("ciudad", models.CharField(max_length=100)),
                (
                    "opciones_envio",
                    models.CharField(
                        choices=[
                            ("GE", "General"),
                            ("EX", "Express"),
                            ("RT", "Recogida en Tienda"),
                        ],
                        default="GE",
                        max_length=18,
                    ),
                ),
                ("creado", models.DateTimeField(auto_now_add=True)),
                ("actualizado", models.DateTimeField(auto_now=True)),
                ("pagado", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-creado"],},
        ),
        migrations.CreateModel(
            name="PedidoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="pedidos.pedido",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pedido_items",
                        to="shop.product",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="pedido",
            index=models.Index(
                fields=["-creado"], name="pedidos_ped_creado_f50ddd_idx"
            ),
        ),
    ]