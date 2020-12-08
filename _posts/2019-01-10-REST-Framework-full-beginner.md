---
layout: post
category: django
title: 'REST Framework full beginner'
---

[ссылка на туториал](https://www.youtube.com/watch?v=B38aDwUpcFc&feature=emb_logo)

(REST Framework documentation)[https://www.django-rest-framework.org/]

# 1. Django project setup

Просто делаем проект, и в нем приложение ```api_basic```. Регаем суперюзера


# 2. Introduction to Serializer

Serializer - "converter data to json"

Сделаем модель Article

```python
# api_basic/models.py
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Регистрируем в settings.py приложение и rest framework

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'rest_framework',
    # Local
    'api_basic.apps.ApiBasicConfig',
]

```

Делаем миграции и мигрируемся.

Регаем модель в админке.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-1.png">

Теперь делаем ```class Serializer``` (это в документации есть), который будет представлять наши данные в  ```json``` формате. Serializer оч похож на Django Forms.

В приложении создаем файл ```serializers.py```. И в нем создаем класс, в котором будут описаны все поля модели.

```python
# api_basic/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
```

Теперь откроем ```django shell``` и проверим работает ли ```ArticleSerializer```

```python
>>> from api_basic.models import Article
>>> from api_basic.serializers import ArticleSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> a = Article(title='Test Article Title', author='Ivan Ivanov', email='ivanov@mail.ru')
>>> a.save()
```

Статья сохранилась и теперь отображается в админке

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-2.png">

Сделаем еще один объект класса Article и затем из него создадим сущность класса Serializer. Затем отрендерим сущность в JSON и в итоге получим serialized data.

```python
>>> from api_basic.models import Article
>>> from api_basic.serializers import ArticleSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> b = Article(title='Branda gets a kettle', author='Branda', email='branda@mail.test')
>>> b.save()
>>> serializer = ArticleSerializer(b)
>>> serializer.data
{'title': 'Branda gets a kettle', 'author': 'Branda', 'email': 'branda@mail.test', 'date': '2020-02-24T19:58:49.819114Z'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"title":"Branda gets a kettle","author":"Branda","email":"branda@mail.test","date":"2020-02-24T19:58:49.819114Z"}'
```

Если нам нужно сериализовать queryset, то сделать это можно с помощью флага ```many```

```python
>>> serializer = ArticleSerializer(Article.objects.all(), many=True)
>>> serializer.data
[OrderedDict([('title', 'Lexus IS 200'), ('author', 'Brenda'), ('email', 'dakuljar@gmail.com'), ('date', '2020-02-24T19:33:37.714806Z')]), OrderedDict([('title', 'DR101'), ('author', 'Dima'), ('email', 'akuulich@gmail.com'), ('date', '2020-02-24T19:33:45.577727Z')]), OrderedDict([('title', 'Honda Civic 5'), ('author', 'William'), ('email', 'wvc@hotmail.com'), ('date', '2020-02-24T19:34:00.051245Z')]), OrderedDict([('title', 'Test Article Title'), ('author', 'Ivan Ivanov'), ('email', 'ivanov@mail.ru'), ('date', '2020-02-24T19:52:40.755228Z')]), OrderedDict([('title', 'Branda gets a kettle'), ('author', 'Branda'), ('email', 'branda@mail.test'), ('date', '2020-02-24T19:58:49.819114Z')])]
```

# 3. Working with Model Serializer

Чтобы посмтореть ModelSerializer немного изменим ```class ArticleSerializer``` на следующий.

```python
# api_basic/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
```

Откроем django shell и посмторим представление.

```python
>>> serializer = ArticleSerializer()
>>> print(repr(serializer))
ArticleSerializer():
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()
```

Как видим, представление осталось то же.


# 4. Working with Functions Based API

Посмотрим как писать ```views.py```.

```python
# api_basic/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import Article
from .serializers import ArticleSerializer

def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        # сериализуем
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```

Напишем теперь urls.py для этого view.

```python
# api_basic/urls.py

from django.urls import path
from .views import article_list

urlpatterns = [
    path('article/', article_list, name='article_list_url')
]
```

И в корневой urls тоже добавим.

Посмторим, что получилось.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-3.png">

Протестим GET запрос с помощью Postman.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-4.png">

Все ОК. Статус 200 ОК.

Теперь протестим POST запрос с помощью Postman.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-5.png">

Получили ошибку, потому что (дальше из документации)

Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as ```csrf_exempt```. This isn't something that you'd normally want to do, and REST framework views actually use more sensible behavior than this, but it'll do for our purposes right now.

Так как мы используем клиент, необходимо использовать декоратор csrf_exempt для вьюхи.

```python
# api_basic/views.py

from django.views.decorators.csrf import csrf_exempt # NEW
# some code below

@csrf_exempt # NEW
def article_list(request):
    if request.method == 'GET':
      # some code below
```

Проверяем еще разе через Postman и все ОК.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-6.png">

Теперь допишем article_detail в views.py.

```python
# api_basic/views.py
@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
```

Допишем url для detail.

```python
# api_basic/urls.py
urlpatterns = [
    path('article/', article_list, name='article_list_url'),
    path('detail/<int:pk>/', article_detail, name='article_detail_url') # NEW
]
```

Тестим detail.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-7.png">


Теперь тестим через Postman.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-8.png">

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-9.png">


# 5. Introduction to api_view() decorator in Function Based API View

Изменим ```article_list``` в ```view.py```.

```python
# api_basic/views.py
from rest_framework.decorators import api_view # NEW
from rest_framework.response import Response # NEW
from rest_framework import status # NEW


@api_view(['GET', 'POST',])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # сериализуем
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-10.png">

Теперь у нас browsible API, откуда мы можем делать запросы. Из Postman тоже работает ОК.

Теперь изменим ```article_detail```.

```python
# api_basic/views.py
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':   
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

Тестим через браузер и все ок.

*Доп инфа. Можем немного изменить поля в serializers.py, добавив туда поле email (или просто написать fields='__all__'). Теперь у нас в API будет отображаться email.*

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-11.png">

# 6. Class Based API View

Сделаем такие же вьюхи, только через Class Based Views

**Делаем list view**

```python
# api_basic/views.py
from rest_framework.views import APIView # NEW

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Пропишем urls.py

```python
# api_basic/urls.py
urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name='article_list_url'), # UPDATED
    path('detail/<int:pk>/', article_detail, name='article_detail_url')
]
```

В браузере все отображается и ничего не изменилось.

**Допишем новый detail.**

```python
# api_basic/views.py
class ArticleDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        # получаем
        article = self.get_object(id)
        # сериализуем
        serializer = ArticleSerializer(article)
        # возвращаем
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

И не забудем изменить urls.py и протестить.

# 7. Working with Generic Views and Mixins

Сделаем list view с помощью generic Views

```python
# api_basic/views.py
from rest_framework import generics # NEW
from rest_framework import mixins # NEW



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        return self.list(request)
```

И не забудем изменить urls.py и протестить.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-12.png">

Добавим возможность create для list view

```python
# api_basic/views.py
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin): # updated
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-13.png">

Добавим PUT и DELETE в views.py

```python
# api_basic/views.py
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
```

Обновим urls.py

```python
# api_basic/urls.py
urlpatterns = [
    path('generic/article/', GenericAPIView.as_view()), # Generic list
    path('generic/article/<int:id>/', GenericAPIView.as_view()), # Generic detail
]
```

# 8. Different type of Authentication like Session Auth, Basic Auth and Token Auth 01:40:40

## Способ 1. BasicAuthentication

Чтобы ограничить доступ к API по сессии определим authentication_classes и permission_classes.

```python
# api_basic/views.py
# code above
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication # NEW
from rest_framework.permissions import IsAuthenticated # NEW

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # code below
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-14.png">

В Postman залогиниться вот так

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-15.png">

## Способ 2. Теперь про TokenAuthentication

Для начала необходимо сделать таблицу, которая будет хранить токены. Откроем settings.py и зарегаем rest_framework.authtoken

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'rest_framework',
    'rest_framework.authtoken', # HERE
    # Local
    'api_basic.apps.ApiBasicConfig',
]
```

Делаем миграцию.

Теперь можем делать токены.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-16.png">

Отредактируем view, чтобы можно было пользоваться токенами.

```python
# api_basic/views.py
# code above
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication # NEW
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication] # EDITED
    permission_classes = [IsAuthenticated]

    # code below
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-17.png">

# 9. Introduction to Viewsets & Routes

Сделаем новые views

```python
# api_basic/views.py

from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class ArticleViewSet(viewsets.ViewSet):
        # если мы используем это viewset, нам необходимо самостоятельно
        # описывать функционал (get, post, create и тп)
        def list(self, request):
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

        def create(self, request):
            serializer = ArticleSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, pk=None): # retrieve это типа detail
            queryset = Article.objects.all()
            article = get_object_or_404(queryset, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        def update(self, request, pk=None): # PUT
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Определим urls с помощью routes (именно их рекомендует документация)

```python
# api_basic/urls.py
# code above
from rest_framework.routers import DefaultRouter # NEW

router = DefaultRouter() # NEW
router.register('article', ArticleViewSet, basename='article') # NEW

urlpatterns = [
    path('viewset/', include(router.urls)), # NEW
    path('viewset/<int:pk>/', include(router.urls)), # NEW
]
```

В итоге получили detail.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-18.png">

И list.

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-19.png">


# 10. Working with Generic Viewsets

Переделаем ArticleViewSet в views.

```python
# api_basic/views.py
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
```

Для list этого и достаточно

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-20.png">

Доступен только GET метод. Добавим POST

```python
# api_basic/views.py
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-21.png">

Добавим PUT (UpdateModelMixin, RetrieveModelMixin)

```python
# api_basic/views.py
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-22.png">

И для Delete добавим mixins.DestroyModelMixin


# 11. Working with Model Viewsets

кусок из документации

## ModelViewSet
The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.
The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

То есть мы можем получить весь функционал PUT, GET, UPDATE, DELETE, CREATE просто вот так.

```python
# api_basic/views.py
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
```

<img src="/assets/img/2019-01-10-REST-Framework-full-beginner/screen-23.png">
