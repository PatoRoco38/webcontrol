import yfinance as yf
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import UserProfile


# View para acessar a página inicial, o @login_required garante que o usuário esteja autenticado
@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            auth_login(request, user)

            next_url = request.POST.get('next') or 'index'
            return redirect(next_url)  # Redireciona para a página inicial após o login bem-sucedido
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
        
    return render(request, 'login.html')

# Função para cadastrar um novo usuário

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

        if User.objects.filter(username=nome_usuario).exists():
            return render(request, 'cadastro.html', {'error': 'Nome de usuário já existe.'})
        
        user = User.objects.create_user(
            username=nome_usuario,
            email=email,
            password=senha
        )

        perfil = UserProfile.objects.create(
            user=user,
            nome_completo=nome,
            data_nascimento=data_nascimento,
            cidade=cidade,
            estado=estado,
            pais=pais,
            telefone=telefone
        )

        return redirect('login')

    return render(request, 'cadastro.html')


def perfil(request):
    return render(request, 'perfil.html')

def sobre(request):
    return render(request, 'sobre.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def candle_data(request):
    import traceback
    from django.http import JsonResponse
    import yfinance as yf

    ticker = request.GET.get('ticker', 'AAPL')
    period = request.GET.get('period', '7d')
    interval = request.GET.get('interval', '1h')

    try:
        data = yf.download(ticker, period=period, interval=interval, auto_adjust=False)

        # Se as colunas forem MultiIndex, aplanar
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']



        required_columns = {'Open', 'High', 'Low', 'Close'}
        if data.empty or not required_columns.issubset(data.columns):
            print(f"Ticker {ticker} retornou dados inválidos ou vazios:")
            print(data.head())
            return JsonResponse({'candles': [], 'error': f'Dados indisponíveis para o ativo {ticker}'}, status=400)

        data.dropna(subset=required_columns, inplace=True)

        ohlc = []
        for index, row in data.iterrows():
            timestamp = int(index.timestamp() * 1000)
            ohlc.append({
                'x': timestamp,
                'y': [
                    round(float(row['Open']), 2),
                    round(float(row['High']), 2),
                    round(float(row['Low']), 2),
                    round(float(row['Close']), 2)
                ]
            })

        return JsonResponse({'candles': ohlc})

    except Exception as e:
        print(f"Erro ao obter dados do ativo {ticker}:")
        traceback.print_exc()
        return JsonResponse({'error': 'Erro interno ao processar os dados.'}, status=500)
