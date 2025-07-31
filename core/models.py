from django.db import models

# Modulo de cadastro de usuários
# Os campos cidade, estado e país estão com valores padrão para facilitar o cadastro
# O campo data de nascimento é opcional, permitindo que o usuário não informe essa informação
# Remoção temporária da classe Cadastro para evitar conflitos
'''
class Cadastro(models.Model):
    nome = models.CharField('nome', max_length=100)
    data_nascimento = models.DateField('dataNascimento')
    cidade = models.CharField('cidade', max_length=100)
    estado = models.CharField('uf', max_length=40)
    pais = models.CharField('pais', max_length=100)
    email = models.EmailField('email', max_length=100)
    telefone = models.CharField('telefone', max_length=15)
    nome_usuario = models.CharField('usuario', max_length=50, unique=True)
    senha = models.CharField('senha', max_length=100)   
    data_cadastro = models.DateTimeField('data de cadastro', auto_now_add=True)


    def __str__(self):
        return f'{self.nome}'
'''
