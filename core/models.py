from django.db import models

class Denuncia(models.Model):
    DENUNCIAS_CHOICES = [
    ("ASSEDIO", "ASSÉDIO (MORAL, SEXUAL, ETC.)"),
    ("DISCRIMINACAO", "DISCRIMINAÇÃO (RAÇA, GÊNERO, IDADE, ETC.)"),
    ("VIOLACAO", "VIOLAÇÕES DE POLÍTICAS DA EMPRESA"),
    ("SEGURANCA", "QUESTÕES DE SEGURANÇA NO TRABALHO"),
    ("OUTROS", "OUTRAS QUESTÕES ESPECÍFICAS"),
]
   
    nome_empresa = models.CharField(max_length=255)
    endereco_empresa = models.CharField(max_length=255)
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
