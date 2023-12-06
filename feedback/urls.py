from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('add/reclamacion/', views.form_reclamacion, name='reclamacion_add'),
    path('list_reclamaciones/', views.list_reclamaciones, name='list_reclamaciones'),

]