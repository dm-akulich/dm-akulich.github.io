---
layout: post
title: 'Асинхронность в Python #6 Корутины и yield from'
category: python
---

## Пример 1  

Корутины (сопрограммы) - это по своей сути генераторы, которые в процессе работы могут принимать извне какие-то данные. Делается это с помощью метода **send**.

```python
def subgen():
    x = 'Ready to accept message'
    message = yield
    print('Subgen received:', message)
```

```yield``` тут справа от равно.

Вызовем код в интерактивном режиме в консоли.

```python
➜  async python -i 5_coroutines.py
>>> g = subgen() # создаем объект генератора
>>> g.send(None) # обязательно передаем ему None, чтобы инициализировать генератор
'Ready to accept message'
>>> g.send('hi')
Subgen received: hi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

*Примечание*: чтобы узнать в каком состоянии находится генератор, можно использовать ```getgeneratorstate``` из модуля ```inspect```.

```python
from inspect import getgeneratorstate
>>> getgeneratorstate(g)
'GEN_CLOSED'
```


## Пример 2

Допустим, есть сайт и каждый днь мы получаем статистику просмотров. И допустим нужно определить среднее значение параметров (среднее арифметическое)

```python
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round((summ / count), 2)
```

Вызовем в интерактивном режиме

```python
➜  async python -i 5_coroutines.py
>>> g = average()
>>> g.send(None)
>>> g.send(1)
1.0
>>> g.send(9)
5.0
>>> g.send(10)
6.67
```

Вызвать исключение можно с помощью метода ```.throw()```.

```python
>>> g.throw(StopIteration)
Done
6.67
```

Чтобы каждый раз не инициализировать генератор с мощью ```.send(None)```, можно использовать специальный инициализирующий декоратор.

```python
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round((summ / count), 2)  
```

В интерактивном режиме проверяем, что все ок и все ок. 

```python
➜  async python -i 5_coroutines.py
>>> from inspect import getgeneratorstate
>>> g = average()
>>> getgeneratorstate(g)
'GEN_SUSPENDED'
>>>
```

## Доп. инфа

Генераторы корутиины могут иметь ключевое слово ```return``` и возвращать некоторое значение. Но получить это значение можно только перехватив исключение.

```python
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            summ += x
            average = round((summ / count), 2)  

    return average
```

В интерактивном режиме

```python
➜  async python -i 5_coroutines.py
>>> g = average()
>>> g.send(5)
5.0
>>> g.send(10)
7.5
>>> try:
...     g.throw(StopIteration)
... except StopIteration as e:
...     print('Average', e.value) # обращаемся к методу value
...
Done
Average 7.5
```

## Делегирующие генераторы и подгенераторы

Делегирующий генератор - это тот генератор, который вызывает другой генератор. Соответственно, подгенератор - тот генератор, который вызывается.

Ситуация такая же как и с обычными функциями, когда мы одни функции вызываем из других. Но есть свли нюансы.

```python
def subgen():
    for i in 'Hello World':
        yield i

def delegator(g):
    for i in g:
        yield i
```

В интерактивном режиме

```python
➜  async python -i 5_1_deleg.py
>>> sg = subgen()
>>> g = delegator(sg)
>>> next(g)
'H'
>>> next(g)
'e'
>>> next(g)
'l'
```

## Корутины вместе с делегирующим генераторами и подгенератором

Задача: чтобы из вызывающего кода передавать на обработку данные через делегирующий генератор.

```python
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

@coroutine
def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('...', message)

@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except:
            pass
```

В интерактивном режиме

```python
➜  async python -i 5_1_deleg.py
>>> sg = subgen()
>>> g = delegator(sg)
>>> g.send('ok')
... ok
>>>
```

### Как передать объект исключения в подгенератор

Делается так. Мы перехватываем объект исключения в делегирующем генераторе. Сохраняем его в переменную. А затем перебрасываем его через метод ```.throw()``` в подгенератор.

```python
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class CustomException(Exception):
    pass

@coroutine
def subgen():
    while True:
        try:
            message = yield
        except CustomException:
            print('Custom exception raised  !!!')
        else:
            print('...', message)

@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except CustomException as e:
            g.throw(e)
```

В интерактивном режиме.

```python
➜  async python -i 5_1_deleg.py
>>> sg = subgen()
>>> g = delegator(sg)
>>> g.send('HI!')
... HI!
>>> g.throw(CustomException)
Custom exception raised !!!
```

## То же самое через yield from в делегирующем генераторе

```python
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class CustomException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except CustomException:
            print('Custom exception raised  !!!')
        else:
            print('...', message)

@coroutine
def delegator(g):
    yield from g
```

В интерактивном режиме.

```python
➜  async python -i 5_1_deleg.py
>>> sg = subgen()
>>> g = delegator(sg)
>>> g.send('HI!')
... HI!
>>> g.throw(CustomException)
Custom exception raised  !!!
```

## Return у подгенератора.

Делегирующий генератор получает то значение, которое возвращает подгенератор с помощью ```return```.

В примере ниже в result попадет значение, возвращаемое с помощью ```return```.

```python
def custom_coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class CustomException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('...', message)
    return 'String from subgen.'

@custom_coroutine
def delegator(g):
    result = yield from g
    print(result)
```

Вызовем код в интерактивном режиме в консоли.

```python
➜  async python -i 5_1_deleg.py
>>> g = delegator(subgen())
>>> g.throw(StopIteration)
String from subgen.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Полученный таким образом результат мы можем как-то дополнительно обработать.

```yield from``` берет на себя передачу данных в подгенератор, передачу исключений, получает возвращаемый с помощью return результат. 

В другиъ языках ```yield from``` называется ```await``` и его смысл в том, что вызывающий код он напрямую управляет работой подгенератора и пока это происходит, делегирующий генератор остается заблокированным. То есть он вынужден ожидать, пока подгенератор закончит свою работу. Подгенератор должен содержать механизм, завершающий его работу. Потому что иначе делегирующий генератор может быть навсегда заблокирован. Пока такого механизмы мы не сделали.


