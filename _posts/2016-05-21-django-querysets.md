---
layout: post
category: django
title: 'Основы Querysets'
---

**Сейчас есть модель поста для блога**

```python
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
```

## Создание объектов

```python
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='admin') # Метод get() возвращает единственный объект из базы данных.
>>> post = Post(title='Post from Shell',
    slug='post-from-shell',
    body='content body from shell',
    author=user)  # создаем объект статьи Post, указав заголовок, слаг и тп 
>>> post.save()
```

## Изменение объектов

```python
>>> post.title = 'Post from Shell (edited)' # Изменение поля объекта
>>> post.save()
```

## Получение объектов

```python
>>> all_posts = Post.objects.all()
>>> Post.objects.all()
```

## Удаление объектов

```python
>>> post = Post.objects.get(id=1)
>>> post.delete()
```

## Другие методы

**Использование метода filter()**

```python
Post.objects.filter(publish__year=2017)
Post.objects.filter(publish__year=2017, author__username='admin')
Post.objects.filter(publish__year=2017).filter(author__username='admin')
```

**Использование метода exclude()**

```python
Post.objects.filter(publish__year=2017).exclude(title__startswith='Why')
```

**Использование метода order_by()**

```python
Post.objects.order_by('title')
Post.objects.order_by('-title')
```

## Создание менеджера модели

objects – менеджер модели по умолчанию. Он возвращает все объекты из базы

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    # ...
    objects = models.Manager() # Менеджер по умолчанию.
    published = PublishedManager() # Наш новый менеджер.
```

Метод менеджера get_queryset() возвращает QuerySet, который будет выполняться. Мы переопределили его и добавили фильтр над результирующим. QuerySet’ом.
Также мы описали менеджер и добавили его в модель Post.Теперь мы можем использовать его для выполнения запросов.

```python
>>> Post.published.filter(title__startswith='Who')
```















