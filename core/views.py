from django.shortcuts import render, redirect  # Importar o redirect do shortcuts, era uma opçao de index
from core.models import Evento  # importando para poder listar os eventos
from django.contrib.auth.decorators import login_required  # Importando o autenticador do django
from django.contrib.auth import authenticate, login, logout  # Para autenticação de login na função submti_login
from django.contrib import messages


# Abaixo estava uma forma opcional de ser fazer o index, optamos por outra
# def index(request):  # Criando um index, minha página principal.
#     return redirect('/agenda/')  # O index irá chamar a agenda.

def login_user(request):  # Definindo função login_user que irá acionar o login.html
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')  # busca usuario digitado
        password = request.POST.get('password')  # busca senha digitada
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")  # Envia esta mensagem para o login.html
    return redirect('/')

# Abaixo o login_url indica o caminho do login caso não tenha um usuário logado
@login_required(login_url='/login/')  # Aplicando decorador que fará uma validação de login para a aplicação.
def lista_eventos(request):
    usuario = request.user  # buscando a informação do usuario
    # evento = Evento.objects.all()  # buscando todos os eventos da agenda com ".all"
    evento = Evento.objects.filter(usuario=usuario)  # buscando eventos da agenda filtrado para o usuario
    dados = {'eventos' : evento}  # passando um dicionario de eventos no response
    return render(request,'agenda.html', dados)  # a função foi criada para renderizar o template criado
                                        # incluído o response no return do html