from django.shortcuts import render, redirect, get_object_or_404
from .models import Denuncia, Cidades, Evidencia
from .forms import NewDenunciaForm, CloseDenunciaForm, UploadEvidencias
from dal import autocomplete
from django.utils.html import format_html


class CidadesAutocomplete(autocomplete.Select2QuerySetView):
        
        def get_queryset(self):
            qs = Cidades.objects.filter()
            if self.q:
                qs = qs.filter(nome__icontains=self.q)
                print(self.q)
            return qs
        
        def get_result_label(self, item):
            return format_html("<p>{}, {}</p>", item.nome, item.estado)
        
      
'''

class CidadesAutocomplete(ListView):
    model = Cidades

    def get_queryset(self):
        queryset =  super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nome__icontains=query)
        return queryset
    
    def get_result_label(self, item):
        return f"{item.nome}, {item.estado}"
'''
def contact (request):
    return render(request, 'core/contact.html')


def index(request):
    if request.method == 'POST':
        form = NewDenunciaForm(request.POST)
        files = UploadEvidencias(request.POST, request.FILES)

        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia = form.save()

        
            file = request.FILES.getlist('imagem')
            for f in file:
                evidencia = Evidencia(denuncia = denuncia, imagem=f)
                evidencia.save()

            return redirect('core:protocol',protocolo=denuncia.protocolo )
    else:     
        form = NewDenunciaForm()
        files = UploadEvidencias()
    return render(request, 'core/index.html',{
        'form': form,
        'files': files,
        'title': 'Nova Denuncia',
    })

def protocol(request, protocolo):
    denuncia = Denuncia.objects.filter(protocolo=protocolo).first()  
    usuario_autenticado = request.user.is_authenticated
    base_template = 'core/base.html'
    evidencia = Evidencia.objects.filter(denuncia = denuncia)

    if request.method == 'POST':
        close = CloseDenunciaForm(request.POST, instance=denuncia)

        if close.is_valid():
            if denuncia.situacao:
                denuncia.situacao = False
            else: 
                denuncia.situacao = True
                
            close = close.save(commit=False)
            close.save()
    else:
        close = CloseDenunciaForm(instance=denuncia)

    if(usuario_autenticado):
        base_template = 'dashboard/base.html'
    return render(request, 'core/protocolo.html', {
        'denuncia': denuncia,
        'evidencia': evidencia,
        'base': base_template,
        'closeForm': close
    })

def pesquisar(request):
    query = request.GET.get('query', '')


    if query:
        return redirect('core:protocol', protocolo=query)

    return render(request, 'core/pesquisar.html', {
        'query': query,
    })