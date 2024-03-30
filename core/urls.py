import djhacker
from django import forms
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('protocolo/<str:protocolo>/', views.protocol, name="protocol"),
    path('cidades-autocomplete/', views.CidadesAutocomplete.as_view(), name='cidades-autocomplete'),
    path('pesquisar/', views.pesquisar, name='pesquisar')
]

 
 