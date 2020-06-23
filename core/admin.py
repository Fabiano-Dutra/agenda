from django.contrib import admin
from core.models import Evento
# Register your models here.

# Criei esta classe para definir os campos da tabela que serão exibidos no resumo da minha agenda
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)  # importante deixar a vírgula no final dentro dos parenteses

admin.site.register(Evento, EventoAdmin)  # associando a classe EventoAdmin a classe Evento para que rode

