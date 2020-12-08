---
layout: post
category: python
title: 'Декораторы'
---

Допустим, у нас есть две функции. В обеих из этих функций есть повторяющийся код. (+это нарушение принципа DRY. А еще это пример того, что генераторы работают быстрее)

```python
from datetime import datetime

def one():
    starttime = datetime.now()
    l = []
    for i in range(10*4):
        if i % 2 == 0:
            l.append(i)

    endtime = datetime.now()
    print(endtime - starttime)
    return l


def two():
    starttime = datetime.now()
    l = [x for x in range(10*4) if x % 2 == 0]
    endtime = datetime.now()
    print(endtime-starttime)
    return l

l1 = one()
l2 = two()
print(l1)
print(l2)

>>> 0:00:00.000055
>>> 0:00:00.000033
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
```

## Делаем декоратор для функций

Декоратор - это типа функция-обертка для другой функции, чтобы избежать дублирования кода.

**Напишем декоратор, который будет считать время функции**

```python
from datetime import datetime

def timeit(func):
    def wrapper():
        starttime = datetime.now()
        result = func()
        endtime = datetime.now()
        print(endtime-starttime)
        return result
    return wrapper

@timeit
def one():
    # starttime = datetime.now()
    l = []
    for i in range(10*4):
        if i % 2 == 0:
            l.append(i)

    # endtime = datetime.now()
    # print(endtime-starttime)
    return l

@timeit
def two():
    # starttime = datetime.now()
    l = [x for x in range(10*4) if x % 2 == 0]
    # endtime = datetime.now()
    # print(endtime-starttime)
    return l

l1 = one()
l2 = two()
# print(l1)
# print(l2)

>>>0:00:00.000028
>>>0:00:00.000014
```


## Функции с аргументами

В функции-декораторе используем args и kwargs

```python
from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        starttime = datetime.now()
        result = func(*args, **kwargs)
        endtime = datetime.now()
        print(endtime-starttime)
        return result
    return wrapper

@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

l1 = one(10*2)
l2 = two(10*2)
print(l1)
print(l2)

>>> 0:00:00.000016
>>> 0:00:00.000008
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

И все работает ок.

Та же конструкция, только вместо *собаки*, может быть представлена в таком виде.

```python
from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        starttime = datetime.now()
        result = func(*args, **kwargs)
        endtime = datetime.now()
        print(endtime-starttime)
        return result
    return wrapper

# @timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


# @timeit
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

what_is_it = timeit(one)
l1 = timeit(one)(10)
print(what_is_it)
print(l1)

>>> 0:00:00.000023
>>> <function timeit.<locals>.wrapper at 0x1038d8160>
>>> [0, 2, 4, 6, 8]
```

## Аргументы у декоратора

Для того, чтобы принимать аргументы у декоратора, нужно дополнительно добавить еще одну обертку. В данном случае это функция outer

```python
def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            starttime = datetime.now()
            result = func(*args, **kwargs)
            endtime = datetime.now()
            print(endtime-starttime)
            return result
        return wrapper
    return outer


@timeit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l
```

Декораторы нужно использовать, когда у нас есть дублирование кода в функциях и этот код не относится к целевому коду функции.















123
