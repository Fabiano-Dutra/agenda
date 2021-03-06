"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views  # importando views para criar uma rota para agenda.html
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),  # rota definida para a função lista_eventos dentro de views
    # Abaixo era uma opção de ser fazer o index, optamos por outra logo abaixo com o redirectview
    # path('', views.index) # Esta era uma opção de caminho index para o navegador já abrir num html definico
    # Abaixo é uma forma mais direta de index sem passar por views, o index escolhido é o agenda.html
    path('agenda/lista/<int:id_usuario>/', views.json_lista_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    # Incluído uma roda para o login
    path('login/', views.login_user),
    path('agenda/evento/', views.evento),  # Rota para a tela de inserção de dados
    path('agenda/evento/submit', views.submit_evento),  # Rota para a função salvar na tela de inserção de dados
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),  # Rota para deletar evento
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]











