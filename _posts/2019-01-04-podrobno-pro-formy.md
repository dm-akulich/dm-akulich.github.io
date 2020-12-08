---
layout: post
category: django
title: 'Подробно про формы'
---

Ссылка на этот проект <a href="https://github.com/dm-akulich/molchanov" target="_blank">тут</a>

## 1. Работа с формами Form, ModelForm, валидация данных

**Создали внутри приложения ```blog``` файл ```forms.py```.**

```python
# blog/forms.py
from django import forms

class TagForm(forms.Form):
    title = forms.CharField(max_length=50) #CharField будет поле input
    slug = forms.SlugField(max_length=50)

    def save(self):  #Переопределяем метод save. Типа все то же самое, что было и в консоли
        new_tag = Tag.objects.create(
            title="self.cleaned_data['title']",
            slug=self.cleaned_data['slug'],
        )
        return new_tag
```

Проверим в ```shell``` консоли работает ли

```python
>>> from blog.models import Tag
>>> from blog.forms import TagForm
>>> d = {'title': 'framework', 'slug': 'framework'}
>>> tf = TagForm(d)
>>> tf.is_bound # Попали ли данные ?
True
>>> tf.is_valid() # Данный валидны ?
True
>>> tf.cleaned_data # Вывод чистыхх данных
{'title': 'framework', 'slug': 'framework'}
>>> t = tf.save()
>>> t
<Tag: self.cleaned_data['title']>
>>> t.id
3
```

**Теперь можем сделать шаблон url'ов для вьюхи которая будет обрабатывать форму**

```python
# blog/urls.py
urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    # path('tag/create/')
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
]
```

```path('tag/create', )``` путь должен быть определен выше пути ```tag/<str:slug>```, потому что если будет ниже,
то django начнет искать в базе тег со слагом create, также пользователь не должен создавать тег "create".

**Чтобы пользователь не мог сделать тег 'create', допишем в Класс ```TagForm``` функцию подчистки слага в forms.py.**

```python
# blog/forms.py
from django import forms
from .models import Tag
from django.core.exceptions import ValidationError # new import

class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=50)

    def clean_slug(self): # new func
        new_slug = self.cleaned_data['slug'].lower()
        
        if new_slug == 'create':
            raise ValidationError("Slug may not be 'create'")

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug must be unique.")

        return new_slug
        

    def save(self):  
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug'],
        )
        return new_tag
```

**Определяем ```url``` путь в ```urls.py``` приложения. С вьюхой ```TagCreate```, которую сделаем потом.**

```python
# blog/urls.py
urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
]
```

**Допишем новый класс ```TagCreate``` в ```views.py```**

Сначала мы должны показать пользователю форму. Обрабатываем GET запрос 
```python
# blog/views.py
### some code above ###
class TagCreate(View):
    def get(self, request): # cначала мы должны показать пользователю форму. GET запрос
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})
### some code below ###

```

**Сделаем шаблон создания тега ```tag_create.html```**

Атрибут ```action``` - это атрибут, который указывает на обработчик этой формы.
т.е. это некая функция, которая будет обрабатываеть данные этой формы после того, как пользвоатель нажмет кнопку. Можно там просто точку поставить и будет ок

```html
<!-- blog/create_tag.html -->
{#% block content %#}

<div class="container">
<form action="{#% url 'tag_create_url' %#}" method="POST">
    {#% csrf_token %#}
    {#{ form.title }#}
    {#{ form.slug }#}
    <button type="submit" class="btn btn-primary">Create Tag</button>
</form>
</div>
{#% endblock content %#}
```

Форма не совсем красивая, допишем под бутстрап.

Дописали форму под бутстраповскую.

```html
<!-- blog/create_tag.html -->
{#% block content %#}

<div class="container">
<form action="{#% url 'tag_create_url' %#}" method="POST">
    {#% csrf_token %#}

    {#% for field in form %#}
    <div class="form-group">
        {#% if field.errors %#}
        <div class="alert alert-danger">
            {#{ field.errors }#}
        </div>
        {#% endif %#}

        {#{ field.label }#}
        {#{ field }#}
    </div>
    {#% endfor %#}
    <button type="submit" class="btn btn-primary">Create Tag</button>
</form>
</div>
{#% endblock content %#}
```

Еще отбработкой занимается джанго, нужно немнгого переопределить поведение класса в ```forms.py```

```python
# blog/forms.py
class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=50)
    title.widget.attrs.update({'class': 'form-control'}) # new
    slug.widget.attrs.update({'class': 'form-control'}) # new
    ### some code below
```

Теперь если мы захотим отправить форму, то вылезет 405 ошибка, потому что мы не определили метод POST

**Реализуем метод POST**

```python
class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        '''
        Логика такая же как в консоли, мы должны создать экземляр класса TagForm с наполненными данными.
        То есть связанную форму.
        Проводим валидацию .is_valid, если все ок, то создаем объект, если нет - рейзим исключение.
        '''
        bound_form = TagForm(request.POST) # создаем cвязанную форму
        if bound_form.is_valid(): # вызываем метод is_valid
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        context = {'form': bound_form}
        return render(request, 'blog/tag_create.html', context=context)
```

**Для придерживания принципов DRY немного передеалем наш ```forms.py```**

```python
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        if new_slug == 'create':
            raise ValidationError("Slug may not be 'create'")
        
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug must be unique.")
        
        return new_slug
```

Выше убрали метод ```save```, потому что у класса ModelForm (связанные модели) есть свой метод.

## 2. Создание Постов через форму, генерация слага, Миксин

### 2.1. Создание поста

Добавляем путь в ```urls.py```.

```python
# blog/urls.py
urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'), # new
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
 		# code below
]
```

Добавляем в ```forms.py``` новую форму ```PostForm```.

```python
# blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
```

Добавляем в ```view.py``` новую ```View```.

```python
class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        
        context = {'form': bound_form}
        return render(request, 'blog/post_create_form.html', context=context)
```


Добавялем шаблон.

```html
<!-- blog/post_create_form.html -->
<form action="{#% url 'post_create_url' %#}" method="POST">
    {#% csrf_token %#}
    {#% for field in form %#}
    <div class="form-group">
        {#% if field.errors %#}
        <div class="alert alert-danger">
            {#{ field.errors }#}
        </div>
        {#% endif %#}

        {#{ field.label }#}
        {#{ field }#}
    </div>
    {#% endfor %#}
    <button type="submit" class="btn btn-primary">Create Post</button>
</form>
```

### 2.2. Генерация слага

В models.py создадим функцию gen_slug. И переопределим метод save, чтобы он подтягивался из функции slug_gen. Использовали время, чтобы уникализировать

```python
from django.utils.text import slugify # new
from time import time # new

def gen_slug(s): # new
    new_slug = slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs): # new
        if not self.id: 
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
```

## 3. Изменение модели

Делаем сразу с миксином 

В view будет 3 "переменных"

```python
# blog/views.py
class TagUpdate(OdjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'

class PostUpdate(OdjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
```

```python
# blog/utils.py
class OdjectUpdateMixin():
    model = None
    model_form = None
    template = None
    
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model__name__.lower(): obj})

```

Добавляем маршруты

```python
# blog/urls.py
from .views import *

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'), # new
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'), # new
]
```

Добавляем шаблоны

```html
<!-- post_update_form.html -->
{#% extends 'base.html' %#}
{#% block title %#} {#{ post.title }#} {#% endblock title %#} - {#{ block.super }#}

{#% block content %#}

<div class="container">
    <form action="{#{ post.get_update_url }#}" method="POST">
        {#% csrf_token %#}
        {#% for field in form %#}
        <div class="form-group">
            {#% if field.errors %#}
            <div class="alert alert-danger">
                {#{ field.errors }#}
            </div>
            {#% endif %#}

            {#{ field.label }#}
            {#{ field }#}
        </div>
        {#% endfor %#}
        <button type="submit" class="btn btn-primary">update Post</button>
    </form>
</div>
{#% endblock content %#}
```

```html
<!-- tag_update_form.html -->
{#% extends 'base.html' %#}
{#% block title %#} Tag Update {#{ tag.title|title }#} {#% endblock title %#} - {#{ block.super }#}

{#% block content %#}

<div class="container">
<form action="{#{ tag.get_update_url }#}" method="POST">
    {#% csrf_token %#}

    {#% for field in form %#}
    <div class="form-group">
        {#% if field.errors %#}
        <div class="alert alert-danger">
            {#{ field.errors }#}
        </div>
        {#% endif %#}

        {#{ field.label }#}
        {#{ field }#}
    </div>
    {#% endfor %#}
    <button type="submit" class="btn btn-primary">Update Tag</button>
</form>
</div>
{#% endblock content %#}
```

## Удаление объектов

Тоже сразу через миксины 

**View.py**

```python

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'post_list_url'

# ##### Переопределили этот класс через Миксин. Оставлю тут, чтобы было понятно, что и без Миксина норм можно делать
# class TagDelete(View):
#     def get(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         return render(request, 'blog/tag_delete_form.html', context={'tag': tag})

#     def post(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         tag.delete()
#         return redirect(reverse('tags_list_url'))
```

**urls.py**

```python
urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'), # new
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url') # new
]
```

**utils.py**

```python
class ObjectDeleteMixin():
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
```

**models.py**

Добавляем *get_delete_url*

```python
class Post(models.Model):
    # some code 
    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})
        ## some code 

class Tag(models.Model):
    # some code 
    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})
        ## some code 
```

**html шаблоны**

```html
{#% extends 'base.html' %#}
{#% block title %#}
    Post Delete {#{ post.title|title }#}
{#% endblock title %#} - {#{ block.super }#}

{#% block content %#}

<div class="container">
<form action="{#{ post.get_delete_url }#}" method="POST">
    {#% csrf_token %#}
    <h3>Are you sure to want delete {#{ post.title|title }#}</h3>
    <a href="{#{ post.get_absolute_url }#}">Cancel</a> 
    <button type="submit" name="button" class="btn btn-danger">Delete Post</button>
</form>
</div>
{#% endblock content %#}
```

```html
{#% extends 'base.html' %#}
{#% block title %#}
    Tag Delete {#{ tag.title|title }#}
{#% endblock title %#} - {#{ block.super }#}

{#% block content %#}

<div class="container">
<form action="{#{ tag.get_delete_url }#}" method="POST">
    {#% csrf_token %#}
    <h3>Are you sure to want delete {#{ tag.title|title }#}</h3>
    <a href="{#% url 'tag_detail_url' slug=tag.slug %#}">Cancel</a> 
    <button type="submit" name="button" class="btn btn-danger">Delete Tag</button>
</form>
</div>
{#% endblock content %#}
```