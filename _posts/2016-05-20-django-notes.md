---
layout: post
category: django
---

*bash команды* 
- "djangonotesedit" - редактировать этот пост
- "djangonotesupdate" - запушить этот пост

## Быстро сделать проект

```bash
mkdir authcustomuser_project && cd authcustomuser_project && python -m venv venv && source venv/bin/activate && pip install django==2.2.8 && pip install pylint && pip install autopep8 && pip freeze > requirements.txt && django-admin startproject authcustomuser_core . && manage.py startapp users && code . && manage.py runserver
```

## Jinja условное выражение по URL


```html
{# if request.get_full_path == "/account/login/" #}
{# endif #}
```

## Пути статиков в settings.py

**Настройки**

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')] # куда мы кладем
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # куда кледет джанго после коллекта
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**urls.py корневого приложения**

```python
# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Автоподтягиваемый slugfield

**Определяем slug в модели**

```python
# models.py
class MyModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
```

**Определяем slug в админке**

```python
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
```

## Как полностью сбросить БД

Шаг 1) inside your project dir Go through each of your projects apps migration folder and remove everything inside, except the ```__init__.py``` file

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

Шаг 2) Drop the current database, or delete the ```db.sqlite3``` if it is your case

Шаг 3) Сделать новую БД

```bash
python manage.py makemigrations
python manage.py migrate
```

## При всяких манипуляциях с БД может вылететь ошибка

```ModuleNotFoundError: No module named 'django.db.migrations.migration'``` или ```...auth```

Фиксится просто переустановкой django в проекте

```bash
pip uninstall Django
pip install Django
```

## Контекст вьюх

Все ключи словаря context - то, что будет использовано в шаблоне

```python
def post_list(request):
    context = {
        'name': 'Ivan Ivanov',
    }
    return render(request, 'blog/index.html', context=context)
```

```html
<body>
    <p>Hello, {#{ name }#}</p>
</body>
```

В результате в браузере будет **hello, Ivan Ivanov** 

Eсли в context находится список, то нужно итерироваться циклом {#% for name in names %#}












