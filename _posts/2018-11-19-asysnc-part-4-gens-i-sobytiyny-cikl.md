---
layout: post
title: 'Асинхронность в Python #4 Генераторы и событийный цикл Round Robin'
category: python
---



Тут пойдет речь о генераторах и событийном цикле построеном по принципу Round Robin (Корусель).

**Немного об особенностях генераторов**

Генераторы - своего рода функции.

## Пример 1

Сделаем простой генератор, который будет 

```python
#generators.py
def gen(s):
    for i in s:
        yield i

g = gen('Dima')
```

Вызовем скрипт в интерактивном режиме

```python
➜  async python -i 3_generators.py
>>> next(g)
'D'
>>> gen
<function gen at 0x10b702400>
>>> 2+2
4
>>> next(g)
'i'
>>>
```

Идея тут в том, что можно поставить выполнение функции на паузу, а потом продолжить ее выполнение с того момента, где она остановилась в прошлый раз.

Функция генератор отдает не только сгенерированный результат, но и контроль выполнения программы. И отдает его в то место, где была вызвана функция next(g)


## Пример 2 с бесконечным циклом

```python
def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time()*1000)
        yield pattern.format(str(t))

g = gen_filename()
```

Запустим в интерактивном режиме

```python
➜  async python -i 3_generators.py
>>> next(g)
'file-1584222279622.jpeg'
>>> next(g)
'file-1584222280597.jpeg'
>>> next(g)
```

**У генераторов после yield можно что-то дописать и оно выполнится. У функций на return все закончится**

```python
def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time()*1000)
        yield pattern.format(str(t))
        
        summa = 123+321
        print(summa)

g = gen_filename()
```

запустим в интерактивном режиме

```python
➜  async python -i 3_generators.py
>>> next(g)
'file-1584222519357.jpeg'
>>> next(g)
444
'file-1584222520181.jpeg'
```

Важно, что несколько yield'ов молжет быть. Генераторы это именно функция.

## Про цикл событий по принципу Round Robin

Round Robin это такой цикл где последовательно элементы заходят в цикл, а после выполнения како-го либо действия обратно становтятся в очередь на выполениние.

```python
def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('dima')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
```

З апустим в интерактивном режиме

```python
➜  async python -i 3_generators.py
d
4
i
3
m
2
a
1
```

Суть примера в том, что генераторы выполнялись строго по очереди. Передавая контродль выполнения строго туда, где вызывалась функция next.














