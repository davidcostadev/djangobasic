# Django Learn Diego

## Instalação

### criar uma virtual env

Aativar virtual env cd nome da virutal_env\Scripts\activate

`py -m venv none_da_virtualenv`

### criar um projeto Django

`django-admin startproject nome_do_projeto .`

### manage.py

## criando app

`py manage.py startapp nome_do_app`

### rodando o server

`py manage.py runserver`

### criar um super usuario para o django admin

`py manage.py createsuperuser`

### criando bando de dados

`py manage.py migrate`

### atualizar o bando de dados

`py manage.py makemigration`

## Usando docker-compose

Subindo o servidor

`docker-compose up -d`

Criando o super usuário

`docker-compose exec web python manage.py createsuperuser`
