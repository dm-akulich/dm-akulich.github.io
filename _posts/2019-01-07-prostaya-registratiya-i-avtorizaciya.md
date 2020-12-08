---
layout: post
category: python
title: 'Простая регистрация, авторизация'
---



# Часть 1. Login и Logout

Добавим в settings.py редиректы при успешном логине и логауте

```python
#settings.py
LOGIN_REDIRECT_URL = 'home_url'
LOGOUT_REDIRECT_URL = 'home_url'
```

В корневой URL добавим путь для аккаунтов

```python
#auth_core/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', include('pages.urls')),
]
```

Сделаем шаблон login по пути templates/accounts/login.html

```html
<!-- templates/accounts/login.html -->
{#% extends 'base.html' %#}
{#% block content %#}
<h2>Log In</h2>
<form method="post">
    {#% csrf_token %#}
    {#{ form.as_p }#}
    <button type="submit">Log In</button>
</form>
{#% endblock content %#}
```

Обновим шаблон home.html

```html
{#% extends 'base.html' %#}
{#% block content %#}
<header>
    <div class="nav-left">
        <h1><a href="{#% url 'home_url' %#}">Django blog</a></h1>
    </div>
</header>
<!-- new -->
{#% if user.is_authenticated %#}
<p>Hi {#{ user.username }#}!</p>
<p><a href="{#% url 'logout' %#}">Log out</a></p>
{#% else %#}
<p>You are not logged in.</p>
<a href="{#% url 'login' %#}">Log In</a>
{#% endif %#}
<!-- /New -->
<h1>I'am home page</h1>
{#% endblock content %#}
```

# Часть 2. Signup

Сделаем приложение accounts ```python manage.py startapp accounts``` и зарегаем его в settings.py

```python
#settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig', #new
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Добавим путь в корневом URL

```python
#auth_core/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), # new
    path('', include('pages.urls')),
]
```

Сделаем urls.py в приложении accounts и сделаем там signup URL помощью SignUpView

```python
# accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
```

Сделаем новую view в приложение accounts

```python
# /accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
```

Определеим шаблон для регистрации в templates/signup.html

```html
<!-- templates/signup.html -->
{#% extends 'base.html' %#}
{#% block content %#}
<h2>Sign up</h2>
<form method="post">
    {#% csrf_token %#}
    {#{ form.as_p }#}
    <button type="submit">Sign up</button>
</form>
{#% endblock content %#}
```

<img src="/assets/img/2019-01-07-prostaya-registratiya-i-avtorizaciya/screen-2.png">

Теперь на сайте готовый логин, логаут, сигнап

# Часть 3. CustomUserModel

- <a href="https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project">Документация по Custom User Model</a>
