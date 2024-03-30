from django.shortcuts import render, redirect
from core import models
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.
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
        
