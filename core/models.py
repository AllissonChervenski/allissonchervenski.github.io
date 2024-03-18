from django.db import models
import datetime
import random


def gerador_protocolo():
    ano_atual = datetime.datetime.now().year

    #Tentativa máximas
    max_tentativas = 20
    tentativas = 0


    while tentativas < max_tentativas:
        rand_num = random.randint(100000, 999999)
        protocolo_novo = f'{ano_atual}{rand_num}'

        if not Denuncia.objects.filter(protocolo=protocolo_novo).exists():
            return protocolo_novo
        tentativas += 1
    
    raise Exception("Erro. Tente novamente mais tarde.")

class Estado(models.Model):
    uf = models.CharField(max_length = 2, unique=True)

    def __str__(self):
        return self.uf

class Cidades(models.Model):
    nome = models.CharField(max_length = 50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

   
    def __str__(self):
        return self.nome

    
class Denuncia(models.Model):
    DENUNCIAS_CHOICES = [
    ("ASSEDIO", "ASSÉDIO (MORAL, SEXUAL, ETC.)"),
    ("DISCRIMINACAO", "DISCRIMINAÇÃO (RAÇA, GÊNERO, IDADE, ETC.)"),
    ("VIOLACAO", "VIOLAÇÕES DE POLÍTICAS DA EMPRESA"),
    ("SEGURANCA", "QUESTÕES DE SEGURANÇA NO TRABALHO"),
    ("OUTROS", "OUTRAS QUESTÕES ESPECÍFICAS"),
]
   
    nome_empresa = models.CharField(max_length=255)
    #cidade = models.CharField(max_length=255)
    #estado = models.CharField(max_length=255)
    endereco_empresa = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidades, related_name='Denuncia', blank=False, null= False, on_delete = models.CASCADE)
    tipo_denuncia = models.CharField( 
        max_length = 13,
        choices = DENUNCIAS_CHOICES
    )
    descricao = models.TextField(blank=False, null=False)

    testemunhas = models.CharField(max_length=255, blank=True, null=True)
    acoes = models.CharField(max_length=255, blank=True, null=True)
    anonimo = models.BooleanField(default=True)
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        unique=False,
     )
    data_ocorrido = models.DateField(blank=True, null=True)
    evidencias = models.ImageField(upload_to='denuncia_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    protocolo = models.CharField(max_length=10, unique=True, default=gerador_protocolo)
    situacao = models.BooleanField(default=True)

    





