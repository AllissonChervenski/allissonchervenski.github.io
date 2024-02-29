from django.shortcuts import render, redirect
from ..core.forms import NewDenunciaForm

def nova_denuncia(request):
    if request.method == 'POST':
        form = NewDenunciaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('denuncia:index')
    else:     
        form = NewDenunciaForm

    return render(request, 'denuncia/form.html',{
        'form': form,
        'title': 'Nova Denuncia'
        
    })