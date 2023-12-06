# Generated by Django 4.1 on 2023-12-06 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=250)),
                ('resolucion', models.CharField(max_length=250)),
                ('estado_reclamacion', models.CharField(choices=[('EN', 'Enviada'), ('BR', 'Bajo Revisión'), ('RE', 'Resuelta')], default='EN', max_length=13)),
                ('num_referencia', models.BigIntegerField(default=0, unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.DecimalField(choices=[(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], decimal_places=1, default=2.5, max_digits=2)),
                ('descripcion', models.CharField(max_length=250)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
