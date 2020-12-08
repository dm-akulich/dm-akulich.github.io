---
layout: post
category: python
title: CustomUserModel, регистрация, авторизация
---

# Часть 1. Создание кастомной модели пользователя
Регаем приложение и AUTH_USER_MODEL

```python
# settings.py
INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTH_USER_MODEL = 'users.CustomUser'
```

сделаем модель пользователя с кастомным полем

```python
# users/views.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
```

Апдейтим две встроенные формы: UserCreationForm and UserChangeForm

Сделаем forms.py в приложении users и апдейтим

```python
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
```

Добавим модель в админку

```python
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
```

Теперь можно проверять. Мигрируем, регаем админа, тестим



# Часть 2. Авторизация

## шаблоны

Сделаем шаблоны и добавим редиректы при логине и логауте в settings.py

```python
#settings.py

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

Создаем шаблоны

```bash
touch templates/registration/login.html
touch templates/base.html
touch templates/home.html
touch templates/signup.html
```

Зададим базовый сразу

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Newspaper App</title>
 </head>
<body>
  <main>
    {#% block content %#}
    {#% endblock content %#}
  </main>
</body>
</html>
```

```html
<!-- templates/home.html -->
{#% extends 'base.html' %#}
{#% block title %#}Home{#% endblock title %#}
{#% block content %#}
{#% if user.is_authenticated %#}
    Hi {#{ user.username }#}!
    <p><a href="{#% url 'logout' %#}">Log Out</a></p>
{#% else %#}
    <p>You are not logged in</p>
    <a href="{#% url 'login' %#}">Log In</a> |
    <a href="{#% url 'signup' %#}">Sign Up</a>
{#% endif %#}
{#% endblock content %#}
```

```html
<!-- templates/registration/login.html -->
{#% extends 'base.html' %#}
{#% block title %#}Log In{#% endblock title %#}
{#% block content %#}
    <h2>Log In</h2>
    <form method="post">
        {#% csrf_token %#}
        {#{ form.as_p }#}
        <button type="submit">Log In</button>
    </form>
{#% endblock content %#}
```

```html
<!-- templates/signup.html -->
{#% extends 'base.html' %#}
{#% block title %#}Sign Up{#% endblock title %#}
{#% block content %#}
<h2>Sign Up</h2>
<form method="post">
    {#% csrf_token %#}
    {#{ form.as_p }#}
    <button type="submit">Sign Up</button>
</form>
{#% endblock content %#}
```

Шаблоны готовы

## URLS

Добавим необходимые URLS в корневой urls.py

```python
# authcustomuser_core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
```

Определим signup в users/urls.py

```python
# users/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
```

Сделаем view для регистрации

```python
# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
```

Теперь необходимо внести изменения в users/forms.py и явно определить там поля

```python
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',) # new
```

<img src="/assets/img/2019-01-08-custom-usermodel-registratiya-i-avtorizaciya/screen-2.png">


Готово. Теперь на сайте готовый логин, логаут, регистрация.

# Часть 3. Добавим логин в другое приложение

Создадим приложение pages ```manage.py startapp pages```. зарегаем его в settings.py, создадим в нем urls.py. В корневом urls.py добавим include на 'pages.urls' ```path('', include('pages.urls')),```

В pages/urls.py сделаем HomeView. Во views.py сделаем view

```python
# pages/urls.py
from django.urls import path
from .views import HomePageView
urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
]
```

```python
# pages/views.py
from django.views.generic import TemplateView
class HomePageView(TemplateView):
  template_name = 'home.html'
```

Добавим в базовый шаблон меню с авторизацей

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  </head>

  <body>
    <title>{#% block title %#}Newspaper App{#% endblock title %#}</title>
    </head>

    <body>
      <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
        <a class="navbar-brand" href="{#% url 'home' %#}">Newspaper</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
          aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          {#% if user.is_authenticated %#}
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link dropdown-toggle" href="#" id="userMenu" data-toggle="dropdown" aria-haspopup="true"
                aria-expanded="false">
                {#{ user.username }#}
              </a>
              <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userMenu">
                <a class="dropdown-item" href="{#% url 'password_change'%#}">Change password</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="{#% url 'logout' %#}">
                  Log Out</a>
              </div>
            </li>
          </ul>
          {#% else %#}
          <form class="form-inline ml-auto">
            <a href="{#% url 'login' %#}" class="btn btn-outline-secondary">
              Log In</a>
            <a href="{#% url 'signup' %#}" class="btn btn-primary ml-2">
              Sign up</a>
          </form>
          {#% endif %#}
        </div>
      </nav>
      <div class="container">
        {#% block content %#}
        {#% endblock content %#}
      </div>
      <!-- scripts -->
    </body>

</html>
```

Все работает

<img src="/assets/img/2019-01-08-custom-usermodel-registratiya-i-avtorizaciya/screen-3.png">
