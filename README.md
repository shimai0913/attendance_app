# attendance_app

## 仮想環境の作成
~~`python -m venv venv`~~

## 仮想環境の有効化
`source venv/bin/activate`

## Pythonパッケージのインストール
`python -m pip install --upgrade pip setuptools`

`python -m pip install django djangorestframework python-dotenv django-cors-headers django-rest-auth django-allauth coreapi PyYAML django-rest-swagger`

`python -m pip install sshtunnel PyMySQL pandas`
sshtunnel PyMySQL pandas

## admin作成
`python manage.py createsuperuser`

## django-rest-swaggerでのエラー
`/venv/lib/python3.8/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html`

~~{% load staticfiles %}~~     =>     {% load static %}

## マイグレーション
`python manage.py migrate`
