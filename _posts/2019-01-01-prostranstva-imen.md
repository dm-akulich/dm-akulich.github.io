---
layout: post
category: django
title: 'Пространства имен'
---

Пространства имен нужны, чтобы в шаблонах мы могли ображаться к конкретному приложению

**Пример**

```python
#blog_app/urls.py
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail, name='post_detail'),
]
```

Определили пространство имен приложения в переменной app_name. Это позволит сгруппировать адреса
для приложения блога и использовать их названия для доступа к ним.

```python
#core_blog/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog'))
]
```

Используемое пространство имен, ```blog```, должно быть уникально по всему проекту.
Мы будем обращаться к шаблонам приложения по пространству имен.
Например ```blog:post_list```, ```blog:post_detail```.

*Подробнее* [тут](https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces)