---
layout: post
title: Генераторы в Python (Coursera. Погружение в Python)
comments: False
category: python
tags:
---

Простейший генератор — это функция, в которой есть оператор **yield**. Что же делает наш генератор? У нас генератор — это **even_range**, который работает по упрощенной схеме знакомого вам генератора range. Он принимает **(start, end)**, записывает текущий **start**, и пока у нас current меньше конечного значения, он **yield'ит current** и прибавляет двойку.

Что же делает этот оператор **yield**? **Yield** можно рассматривать как какой-то временный **return**, то есть у нас возвращается значение **current**.
Однако выполнение функции не прекращается, это не обычный **return**,
return, как вы видите, здесь вот в конце, у нас **return None** по умолчанию.
**Yield** возвращает значение, но прерывает выполнение функции только на время, то есть мы можем вернуться к этой функции, к этому моменту.
Важно знать, что мы можем итерироваться, например, по генератору, можем пробежаться и вывести все значения. Каждый раз, когда у нас выполняется **yield**, у нас возвращается значение **current**, и каждый раз, когда мы просим следующий элемент, у нас выполнение функции возвращается в этот же момент, и мы идем дальше.  

```python
def enev_range(start: int, end: int) -> int:
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(0, 10):
    print(number)
```

Чтобы посмотреть, как это происходит на самом деле, можно воспользоваться функцией **next**, которая действительно применяется каждый раз при итерации.

```python
ranger = even_range(0, 4)
next(ranger)
>>> 0
next(ranger)
>>> 2
```


```python
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b
```

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
print(next(generator))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(3)))

>>> 0
>>> Got: 1
>>> Accumulated: 1
>>> Got: 3
>>> Accumulated: 4

```
