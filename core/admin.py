from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome_completo', 'data_nascimento', 'telefone', 'cidade', 'estado', 'pais')
    search_fields = ('user__username', 'nome_completo', 'telefone', 'cidade', 'pais')