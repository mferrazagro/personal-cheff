# Personal Cheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="example.jpg" alt="exemplo Python">
>Uma aplicação web de receitas chamada PersonalCheff desenvolvida durante o curso de Python no Senac de Americana. A aplicação listará receitas e clicando em cada nome de receita você pode ver a receita completa.

### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
- [X] Instalar o Python
- [X] Instalar Visual Studio Code

```
NÃO ESQUECER DE MUDAR TERMINAL PARA CMD
para ativar ambiente virtual:
python -m venv. \venv\
venv\Scripts\activate
```
- [X] Criar e ativar o ambiente virtual
- [X] Instalar o Django
```
para instalar o DJANGO
python -m pip install django==3.2
```
- [X] Criar o projeto PersonalCheff
```
Exibir os principais comandos do Django:
django-admin.py help 

Para Startar o projeto:
django-admin.py startproject 'nomedoprojeto'
```
- [X] Subir o servidor e testar o projeto
```
abrir a pasta cd 'nomedapasta

Subir o servidor e executar a aplicação:
python manage.py runserver

```

- [X] Alterar o idioma do projeto para `pt-br`
```
para alterar o idioma, abrir settings.py linha 106, mudar para pt-br
```
- [X] Alterar o timezone do projeto para `America/Sao_Paulo`
- [X] Criar o app receitas
```
preciso estar dentro da pasta do projeto (PersonalcheffProj)
python manage.py startapp receitas
```
- [X] Registrar o app receitas
```
no arquivo settings.py adicionar o app receitas na lista de apps 
INSTALLED_APPS
[
    ...
    'receitas',
]
```
- [X] Configurar a rota inicial (index)
```
    Dentro da pasta receita(app) criar o arquivo urls.py
    No arquivo urls.py
    
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index')
    ]
```

- [X] Criar a view para a rota inicial
    Dentro da pasta receitas(app) abrir o arquivo views.py
```
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Seja bem vindo</h1>")
```
- [X] Registrar a rota inicial

```
Dentro da pasta PersonalCheffProj(app) abrir o arquivo urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('receitas.urls')),
]
```
- [X] Criar o arquivo index
 - Dentro da pasta receitas (app), crie a pasta `templates`
 - Dentro da pasta `templates` criar `index.html`
 - No arquivo `views.py` que está dentro da pasta do app faça a seguinte alteração de código:
 ```
 python
 ```
 - [X] Integrar arquivos estáticos (CSS, JS)
 - Dentro da pasta do projeto (PersonalCheffProj), criar a pasta `static`
 - Dentro da pasta static, colocar as imagens, os arquivos css e os arquivos js que for utilizar
 - No arquivo `settings.py`:
    - realize a importação da biblioteca `os` através do comando `import os`
    - na linha ~*58* adicione o caminho dos templates da seguinte forma:
  
    ```python
    'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],
    ```
    
    - No final do arquivo, após a linha ´STATIC_URL´, insira o seguinte código:
    ´´´
    STATIC_ROOT = os.path.join(BASE_DIR, 'static)
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'PersonalCheffProj/static')
    ] 
    ```
    - `STATIC_URL`: é a configuração da rota através do qual os arquivos estáticos seram servidos
    - `STATIC_ROOT`: configuração da pasta de saída (destino) dos arquivos estáticos
    - `STATICFILES_DIRS`: configuração da(s) pasta de origem dos arquivos estáticos
    - após realizar essas configurações execute, no terminal o comando:
    `python manage.py collectstatic` 
    - na primeira linha do arquivo `index.html` insira `{% load static %}. Esse comando deve ser usado em todos os arquivos em que você for utilizar arquivos estáticos.
    - insira uma imagem usando o comando <img src="{% static 'logo.png' %}">`. Sempre que for utilizar um arquivo estático você deve utilizar {% static 'nome-do-arquivo' %}
    
- [ ] Utilizando links
 
 []Criando o base.html
 
 []Separando em partials
 
 []Renderizando dados dinamicamente
 
 []Criando um dicionario com as receitas
 
 []Criando o banco de dados(MySQL/MariaDB)
 
 []Instalando o conector do bando de dados MySQL
 
 []Criando o modelo da receita
 
 []Criando a migration (mapeamento)
 
 []Realizando a migration
 
 []Registrando um modelo no admin
 
 []Criando um usuário para o ambiente administrativo
 
 ## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo]<br>