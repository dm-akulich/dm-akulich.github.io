---
layout: post
category: django
title: 'Отправка электронной почты с Django'
---

Отправка сообщений может быть реализована средствами Django. Для начала
необходимо установить локальный SMTP-сервер или сконфигурировать доступ к 
внешнему SMTP-серверу, добавив следующие настройки в ```settings.py```
проекта:

- EMAIL_HOST – хост SMTP-сервера; по умолчанию localhost;
- EMAIL_PORT – порт SMTP-сервера; по умолчанию 25;
- EMAIL_HOST_USER – логин пользователя для SMTP-сервера;
- EMAIL_HOST_PASSWORD – пароль пользователя для SMTP-сервера;
- EMAIL_USE_TLS – использовать ли защищенное TLS-подключение;
- EMAIL_USE_SSL – использовать ли скрытое TLS-подключение.

Если нельзя использовать SMTP-сервер, можно дать Django указание записывать адреса в консоль,
добавив такую настройку в ```settings.py```:

```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'```

При задании этой настройки Django будет выводить e-mail-сообщения в консоль. Это может быть полезно при тестировании приложения без подключения
к SMTP-серверу.
Если вы хотите отправлять сообщения, но на вашем компьютере не установлен локальный почтовый сервер, можете использовать SMTP-сервер вашего почтового провайдера. Следующая конфигурация позволяет отправлять
e-mail-сообщения, используя Gmail-сервер и ваш аккаунт Google:

```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```


Тестим с помощью ```python manage.py shell``` отправку письма:

```python
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'This e-mail was sent with Django.',
    'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)
```

Функция ```send_mail()``` принимает в качестве обязательных аргументов тему,
сообщение, отправителя и список получателей.
Указав дополнительный параметр ```fail_silently=False```, мы говорим, чтобы при сбое в  отправке сообщения
было сгенерировано исключение. Если в результате выполнения вы увидите 1,
ваше письмо успешно отправлено.
Если вы используете Gmail, нужно также разрешить доступ на странице

```https://myaccount.google.com/lesssecureapps```







