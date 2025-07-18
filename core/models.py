from django.db import models

# Modulo de cadastro de usuários
class Cadastro(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=100)
    telefone = models.CharField('Telefone', max_length=15, blank=True, null=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)