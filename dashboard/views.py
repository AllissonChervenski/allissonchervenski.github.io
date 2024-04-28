from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core import models
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.

@login_required
def index(request):
    lista = models.Denuncia.objects.all()
    return render(request, 'dashboard/index.html',  { 
        'lista': lista,
    })

def protocol(request, protocolo):
    lista = models.Denuncia.objects.all()
    if request.method == 'GET':
        return redirect('core:protocol',protocolo=protocolo)
    else:
        return render(request, 'dashboard/index.html', {
        })
    