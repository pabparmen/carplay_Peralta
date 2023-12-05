from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('create/', views.pedido_create, name='pedido_create'),
]