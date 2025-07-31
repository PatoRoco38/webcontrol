from django.db import models
from django.contrib.auth.models import User

# Modulo de cadastro de usuários
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField('nome', max_length=100, null=True, blank=True)
    data_nascimento = models.DateField('dataNascimento', null=True, blank=True)
    cidade = models.CharField('cidade', max_length=100, null=True, blank=True)
    estado = models.CharField('uf', max_length=40, null=True, blank=True)
    pais = models.CharField('pais', max_length=100, null=True, blank=True)
    telefone = models.CharField('telefone', max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'


