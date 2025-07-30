from django.urls import path
from .views import index, login, cadastro, perfil, sobre, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('sobre/', sobre, name='sobre'),
    path('dashboard/', dashboard, name='dashboard'),
]