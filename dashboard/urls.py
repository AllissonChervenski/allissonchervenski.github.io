from django import forms
from django.urls import path
from . import views

app_name="dashboard"

urlpatterns = [
    path('', views.index, name="index" ),
    path('protocolo/<str:protocolo>/',  views.protocol, name="protocol")
]
