from django.shortcuts import render # ,redirect  # Importar o redirect do shortcuts, era uma opçao de index
from core.models import Evento  # importando para poder listar os eventos


# Abaixo estava uma forma opcional de ser fazer o index, optamos por outra
#def index(request):  # Criando um index, minha página principal.
#    return redirect('/agenda/')  # O index irá chamar a agenda.

def lista_eventos(request):
    evento = Evento.objects.all()  # buscando todos os eventos da agenda com ".all"
    dados = {'eventos' : evento}  # passando um dicionario de eventos no response
    return render(request,'agenda.html', dados)  # a função foi criada para renderizar o template criado
                                        # incluído o response no return do html