import csv
from .models import Estado, Cidades

def load_estados():
       
    with open('./Municipios_normalizados.csv', 'r', encoding='latin-1') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
            estado_nome = row['Chave']
            cidades_nomes = [cidade.strip() for cidade in row['Valores'].split(',')]

            # Verificar se o estado já existe
            estado, created = Estado.objects.get_or_create(uf=estado_nome)

            # Adicionar cidades ao estado
            for cidade_nome in cidades_nomes:
                cidade, _ = Cidades.objects.get_or_create(nome=cidade_nome, estado_id=estado.id)

        


