# attendance_app
## 勤怠システムAPI (http://3.138.245.157:8000/api/)

### Siri,LINE, モバイルアプリ、モバイルアプリ(開発中)と連携して使用

## 仮想環境の作成
~~`python -m venv venv`~~

## 仮想環境の有効化
`source venv/bin/activate`

## Pythonパッケージのインストール
`python -m pip install --upgrade pip setuptools`

`python -m pip install django djangorestframework python-dotenv django-cors-headers django-rest-auth django-allauth coreapi PyYAML django-rest-swagger django-environ`

`python -m pip install sshtunnel PyMySQL pandas`

## 環境変数の管理
`cp .env.example .env`

`.env`の修正 

## マイグレーション
`python manage.py migrate`

## admin作成
`python manage.py createsuperuser`

## django-rest-swaggerでのエラー
`/venv/lib/python3.8/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html`を修正

~~{% load staticfiles %}~~

{% load static %}

uwsgi --ini rakudasu_project_uwsgi.ini
