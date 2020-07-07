from django.contrib.auth.models import User
from django.shortcuts import render, redirect  # Importar o redirect do shortcuts, era uma opçao de index
from core.models import Evento  # importando para poder listar os eventos
from django.contrib.auth.decorators import login_required  # Importando o autenticador do django
from django.contrib.auth import authenticate, login, logout  # Para autenticação de login na função submti_login
from django.contrib import messages
from datetime import datetime, timedelta  # Importando datetime para comparar hora atual com do evento
from django.http.response import Http404, JsonResponse

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
    data_atual = datetime.now() - timedelta(hours=1)  # Criando string data_atual
    evento = Evento.objects.filter(usuario=usuario,  # buscando eventos da agenda filtrado para o usuario
                                    data_evento__gt=data_atual)  # __gt compara se está acima da data atual
    dados = {'eventos' : evento}  # passando um dicionario de eventos no response
    return render(request,'agenda.html', dados)  # a função foi criada para renderizar o template criado
                                        # incluído o response no return do html

@login_required(login_url='/login/')
def evento(request):  # Criado a função evento para chamar o evento.html para inserção de dados
    id_evento = request.GET.get('id')
    dados = {}  # Se não tiver id é porque é a inserção de um evento novo então dados estará em branco.
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        #local_evento = request.POST.get('local_evento')
        descricao = request.POST.get('descricao')
        usuario  = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:  # Aqui está validando o usuário antes de fazer a alteração
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            # Abaixo está uma opção de se fazer a alteração de um registro usando outro comando
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):  # Função para deletar eventos
    usuario = request.user    # Buscando identificação do usuário.
    try:
        evento = Evento.objects.get(id=id_evento)  # Identificação do evento.
    except Exception:
        raise Http404()  # Na exceção dará erro 404
    if usuario == evento.usuario:  # Validando se o usuário é o dono do evento.
        evento.delete()   # Deletar se sim.
    else:
        raise Http404()  # Dará erro 404
    return redirect('/')

#@login_required(login_url='/login/')
#def json_lista_evento(request):
#    usuario = request.user  # buscando a informação do usuario
#    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')  # buscando eventos da agenda filtrado para o usuario
#    return JsonResponse(list(evento), safe=False)  # Retorna o JsonResponse

# Outra opão de fazer o json para enviar uma resposta:
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)

