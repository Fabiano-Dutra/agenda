from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Para a agenda funcionar preciso de uma tabela para manipular esta agenda
# a tabela terá informações sobre o evento como: título, data, data de criação
# Então será criada a tabela Eventos


class Evento(models.Model):
    titulo = models.CharField(max_length=100)  # Charfield título, com tamanho 100, não pode ser em branco
    descricao = models.TextField(blank=True, null=True)  # não tem tamanho limite, mas pode ser branco ou nulo
    data_evento = models.DateTimeField(verbose_name="Data do Evento")  # não pode ser nulo, então fica sem parâmetro null
    data_criacao = models.DateTimeField(auto_now=True)  # com este parâmetro auto_now é automático, não será preenchido
                                                        # pelo usuário, ele sempre irá preencher com a hora atualizadapy
    # Os eventos precisam de um usuário para identificar seu dono
    # então será usada a tabela de usuários criada no primeiro exercício
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # usando um usuário estrangeiro, o cascade é para qdo
                                                                # for deletar o usuário tb delete as outras infos dele
    class Meta:
        db_table = 'evento'  # Está exigindo que minha tabela se chame evento

    def __str__(self):  # colocar aqui a explicação da ultima aula do modulo 2
        return self.titulo

    def get_data_evento(self):   # Alterando o formato de data apresentado no html
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')  # Novo formato de data e tb incluindo hora e minutos

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False