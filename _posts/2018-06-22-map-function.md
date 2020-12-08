---
layout: post
category: python
title: 'Функция map в python'
---

Можно сказать, что функия map в python это элемент функцияонального программирования. Фунция принимает на вход минимум два аргумента.

```python
map(func, *iterable)
```

Первым агрументом она принимает некоторую функцию обработчик, вторым аргументом принимает некоторый итерируемый объект. Итерируемых объектов может быть несколько, но чаще всего это один объеки и он список.

Задача функции: она применяет переданную ей функцию-обработчик к каждому элементу переданного ей списка (или другого иерируемого объекта)

Возвращает функция map object, который является **итератором**, который при желании можно преобразовать в список.

Небольшой пример:

```python
def upper(string):
    return string.upper()

l = ['one', 'two', 'three']

new_list = map(upper, l)
print(new_list)

>>> <map object at 0x103f90400>
```

Чтобы посмотреть содержание map объекта, можно преобразовать его в list.

```python
new_list = list(map(upper, l))

>>> ['ONE', 'TWO', 'THREE']
```

Фунция map эквивалентна коду

```python
def map(func, iterable):
    for i in iterable:
        yield func(i)
```

Так ка кmap object является итераторо, его можно прогонять через цикл for.

Часто фунцию map можно встретить с lambda функциями. Преобразуем map object в список с момощью lambda функции.

```python
new_list = list(map(lambda string: string.upper(), l))
print(new_list)

>>> ['ONE', 'TWO', 'THREE']
```

Если нам нужно именно список, а не итератор, то можно это сделать с помощью генератора списков.

```python
new_list = [string.upper() for string in l]
print(new_list)

>>> ['ONE', 'TWO', 'THREE']
```





















123
