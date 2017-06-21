"""HiFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^login/', login),
	url(r'^logout/', logout),
	url(r'^cadastro/', cadastro),
    url(r'^gerenciar/', gerenciar),
    url(r'^confirmar/$', confirmar),
    url(r'^perfil/$', perfil),
    url(r'^estatisticas/$', estatisticas),
    url(r'^valida-token-senha/$', valida_token_senha),
    url(r'^recuperar/', recuperar),
    url(r'^alterar-senha/', alterar_senha),
    url(r'^amigos/', amigos),

    url(r'^seguir/(?P<uid>\w+)/', seguir),
    url(r'^dseguir/(?P<uid>\w+)/', deixar_de_seguir),

    url(r'^associar/(?P<uid>\w+)/', associar),
    url(r'^dassociar/(?P<uid>\w+)/', deixar_de_associar),

    url(r'^chat/$', chat),
    url(r'^chat/(?P<uid>\w+)/$', chat),
]
