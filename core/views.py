from django.shortcuts import render, redirect, get_object_or_404
from .models import Denuncia, Cidades
from .forms import NewDenunciaForm
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