from django.contrib import admin

# Register your models here.
from .models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cidade', 'estado', 'pais')
    search_fields = ('nome', 'email')

admin.site.register(Cadastro, CadastroAdmin)
