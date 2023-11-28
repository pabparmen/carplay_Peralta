from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('datos/', views.datos, name='datos'),

]