# Formulário de Denúncia de negligência a saúde do trabalhador

O formulário de denúncia de negligência a saúde do trabalhador foi desenvolvido usando o framework Django. O formulário tem o objetivo de facilitar a denúncia de problemas no ambiente de trabalho, em contato com a equipe de segurança do trabalho.

## Recursos Principais

- Envio dos detalhes da denúncia através de um formulário.
- Denúncia anônima ou não, contendo atualizações por e-mail caso não seja.
- Acompanhamento da situação da denúncia.
- Contato com a equipe da segurança do trabalho.
- Painel de administração para gerenciamento de denúncias.


## Configuração do Ambiente

1. **Pré-requisitos:**
   Certifique-se de ter o Python e o Django instalados em sua máquina.

2. **Clone o repositório:**
   ```bash
   git clone https://github.com/AllissonChervenski/denuncia_forms.git
   cd forms_denuncia
   ```

3. **Configuração do Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # Ou
   .\venv\Scripts\activate  # Windows
   ```
4. **Instalando dependências:**
   Instale as dependências no ambiente virtual
   ```bash
   python -m pip install Django
   python -m pip install Pillow
   ```

5. **Configuração do Banco de Dados:**
   ```bash
   python manage.py migrate
   ```

6. **Execute o Servidor de Desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a Aplicação:**
   Abra o navegador e acesse `http://127.0.0.1:8000/`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
