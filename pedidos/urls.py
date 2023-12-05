from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('create/', views.pedido_create, name='pedido_create'),
    path('admin/pedido/<int:pedido_id>/', views.admin_pedido_detail,
    name='admin_pedido_detail'),
    path('admin/pedido/<int:pedido_id>/pdf/',views.admin_pedido_pdf,
         name='admin_pedido_pdf'),
]