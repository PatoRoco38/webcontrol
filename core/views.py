from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from core.models import Cadastro
from django.contrib.auth.hashers import make_password


# View para acessar a página inicial, o @login_required garante que o usuário esteja autenticado
@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        try:
            user = Cadastro.objects.get(nome_usuario=usuario, senha=senha)
            request.session['usuario_id'] = user.id
            return redirect('index')  # Redireciona para a página inicial após o login bem-sucedido
        except Cadastro.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
        
    return render(request, 'login.html')

def index(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    return render(request, 'index.html')

# Função para cadastrar um novo usuário
@login_required
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('dataNascimento')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('uf')
        pais = request.POST.get('pais')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')

        if senha != confirmar_senha:
            return render(request, 'cadastro.html', {'error': 'As senhas não conferem.'})

        Cadastro.objects.create(
            nome=nome,
            data_nascimento=data_nascimento,
            cidade=cidade,
            estado=estado,
            pais=pais,
            email=email,
            telefone=telefone,
            nome_usuario=nome_usuario,
            senha=make_password(senha)  
        )
        return redirect('login')

    return render(request, 'cadastro.html')


def perfil(request):
    return render(request, 'perfil.html')

def sobre(request):
    return render(request, 'sobre.html')

def dashboard(request):
    return render(request, 'dashboard.html')