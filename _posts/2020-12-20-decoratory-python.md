---
layout: post
title: Декораторы в Python (Crs. Погружение в Python)
comments: False
category: python
tags:
---

# Декораторы

Декораторы - функция, которая принимает одну функцию и возвращает другую функцию.

Пример простейшего декоратора.

Cинтаксис такой: 
```python
def decorator(func):
    return func

@decorator
def decorated():
    print("hello!")
```

На самом деле происходит это. Вызывается декоратор, в него передается функция, и все записывается в функцию, которую мы декорируем.

```python 
decorated = decorator(decorated)
```

Часто бывает необходимо вернуть не ту же самую функцию, а какую-то модифицированную функцию или вообще новую функцию совершенно другую. Например, ещё один простой декоратор, мы можем его определить, он принимает функцию, определяет внутри какую-то новую функцию и возвращает её. 

Чаще всего декораторы используются для того, чтобы модифицировать поведение каких-то функций. Часто бывает необходимо использовать один декоратор, для того чтобы какое-то семейство функций переопределить, модифицировать их поведение. 

Написав один декоратор, мы можем модифицировать поведение сразу многих функций. 

**Написать декоратор, который записывает в лог результат декорируемой функции.**

Мы хотим, чтобы в лог (файл) записывался результат функции, к которой был применен декоратор.

```python
def logger(func):  # 1. Определили декоратор
    def wrapped(num_list):  # 2. То, что мы переопределяем
        result = func(num_list) # Функция получает результат работы summator'a.
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)

summator([1, 2, 3, 4, 5])
>>> 15
```

Применяя декоратор, мы подменяем функцию **summator** новой функцией **wrapped**, и именно она уже будет выполняться. Эта функция новая, она принимает **num_list**, так же как и **summator**, получает результат работы **summator'а**, записывает результат в файл и просто возвращается. 

Бывает полезно определить декоратор так, чтобы он мог применяться не только к функциям, которые принимают **num_list**, а, например, к функциям, которые принимают любое количество аргументов, любое количество параметров. Как вы могли догадаться, нам нужно нашу функцию определить так, чтобы она принимала любое количество аргументов. 

```python
def logger(func):  # 1. Определили декоратор
    def wrapped(*args, **kwargs):  # 2. То, что мы переопределяем
        result = func(*args, **kwargs)
        with open('log.txt', 'a+') as f:
            f.write(str(result))
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)

@logger
def printer_multiplier(text: str, num: int) -> str:
    return text*num


summator([1, 2, 3, 4])
printer_multiplier('Hello ', 5)

with open('log.txt', 'r+') as f:
    print(f.readlines())
```

**Написать декоратор с параметром, который записывает лог в указанный файл**

Есть наш новый декоратор, который принимает уже не функцию, а принимает **filename**. Собственно, записывает в этот **filename** результат выполнения функции. Что должен вернуть наш декоратор? Он должен вернуть декоратор, то есть, на самом деле, у нас можно рассматривать **logger** не как декоратор, а как просто функцию, которая возвращает декоратор.
И возвращает она декоратор, который принимает функцию. Таким образом, мы вызовем **logger** вначале, у нас вернётся декоратор, и потом этот декоратор уже будет применяться к функции **summator**. 

```python
def logger(filename): # 2. вызывается функция, куда передаем имя
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a+') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)


@logger('old_log.txt')
def printer_multiplier(text: str, num: int):
    return text*num


summator([1, 2, 4, 5, 3, 1])
printer_multiplier('hellw', 3)

with open('new_log.txt', 'r') as f:
    print(f.readlines())

with open('old_log.txt', 'r') as f:
    print(f.readlines())

>>> ['16']
>>> ['hellwhellwhellw']
```

## Пример с двумя декораторами

```python
def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@bold
@italic
def hello():
    return "Hello World"

print(hello())

>>> <b><i>Hello World</i></b>
```
