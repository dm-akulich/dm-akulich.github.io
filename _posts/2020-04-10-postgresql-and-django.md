---
layout: post
category: django
title: 'PostgreSQL и Django'
tags: sql, django
---

# Заметки Django. Модель и миграции на Postgres
Откроем сначала консоль Postgres и создадим БД 

```sql
postgres=# CREATE DATABASE dronovdb OWNER postgres;
postgres=# \l
```

Переходим в venv и установим модули для работы с Postgres

```bash
$ pip install psycopg2
$ pip install psycopg2-binary
```

Далее поставим наши параметры БД в settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dronovdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    }
}
```

Мигрируем

```bash
$ python manage.py migrate
```

В нашем приложении bboard есть тестовая модель в models.py

```python
from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
```

Создадим миграцию 

```bash
$ python manage.py makemigrations
```

Проверим работает ли все ок и создадим запись в БД. Открываем консоль Django

```python
>>> from bboard.models import Bb
>>> b2 = Bb(title="БМВ", content="Не бита не крашена. 1986", price="2500")
>>> b2.save()
>>> b2.title
'БМВ'
```

Теперь выведем это на страницу. Для этого настроим наш views.py уровня bboard

```python
from django.shortcuts import render
from django.http import HttpResponse

from bboard.models import Bb

def bboard(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
```

Все ок. На странице выводятся объявления

## Шаблоны
Немного приукрасим, и подгрузим это из шаблона. Для этого отредачим немного views.py

```python
# Исправленный views.py

def bboard(request):
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return render(request, 'index.html', context)
``` 

Подгрузим сам html шаблон

```html
<!DOCTYPE html> 
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Главная - доска объявлений</title> 
</head>
<body>
    <h1>объявления</h1>
    {#% for bb in bbs %#}
    <div class="">
        <h2>{#{ bb.title }#}</h2>
        <p> {#{ bb.content }#}</p>
        <p>{#{ bb.published|date:"d.m.Y Н:i:s" }#}</p>
        <span><strong>{#{ bb.price }#}</strong></span>
    </div>
    {#% endfor %#}
</body>
</html>
```

Отобразим модель в админке, отредактировав admin.py 

```python
from django.contrib import admin
from bboard.models import Bb
admin.site.register(Bb)
```