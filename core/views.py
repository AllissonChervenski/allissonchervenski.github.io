from django.shortcuts import render, redirect

from .forms import NewDenunciaForm

def contact (request):
    return render(request, 'core/contact.html')

def index(request):
    if request.method == 'POST':
        form = NewDenunciaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('core:index')
    else:     
        form = NewDenunciaForm

    return render(request, 'core/index.html',{
        'form': form,
        'title': 'Nova Denuncia',
        'header_text': 'Formulário de denúncia de negligência a saúde do trabalhador',
    })
