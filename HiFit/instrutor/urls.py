from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regras', views.regras, name='regras'),
]