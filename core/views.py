from django.shortcuts import render, redirect, get_object_or_404
from .models import Denuncia
from .forms import NewDenunciaForm

def contact (request):
    return render(request, 'core/contact.html')

def index(request):
    if request.method == 'POST':
        form = NewDenunciaForm(request.POST, request.FILES)

        if form.is_valid():
            denuncia = form.save()

    
            return redirect('core:protocol',protocolo=denuncia.protocolo )
    else:     
        form = NewDenunciaForm()

    return render(request, 'core/index.html',{
        'form': form,
        'title': 'Nova Denuncia',
    })

def protocol(request, protocolo):
    denuncia = Denuncia.objects.filter(protocolo=protocolo).first() 

    return render(request, 'core/protocolo.html', {
        'denuncia': denuncia,
    })