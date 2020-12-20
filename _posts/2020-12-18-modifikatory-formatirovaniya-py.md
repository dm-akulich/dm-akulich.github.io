---
layout: post
title: Модификаторы форматирования в Python (Crs. Погружение в Python)
comments: False
category: python
tags:
---

# Модификаторы форматирования строк
## 1-й способ форматирования через плейсхолдеры

```python
template = "%s My Awesome template is - %s"
print(template % ('Hello', 'bitch'))
>>> Hello My Awesome template is - bitch
```

## 2-й способ форматирования
```python
template_2 = "{} My Awesome template is - {}"
print(template_2.format('Hello', 'bitch'))
>>> Hello My Awesome template is - bitch
```

## 3-й способ форматирования
```python
template_2 = "{name} My Awesome template is - {second}"
print(template_2.format(name='Hello', second='bitch'))
>>> Hello My Awesome template is - bitch
```

## 4-й способ форматирования
```python
name = 'Hello'
second = 'bitch'
print(f"{name} My Awesome template is - {second}")
>>>  Hello My Awesome template is - bitch
```

# Модификаторы форматирования чисел
## вывод в двоичном виде
```python
num = 8
print(f"Binary: {num:#b}")
>>> Binary: 0b1000
```

## вывод до третьего знака после запятой
```python
num_2 = 2 / 3
print(f"{num_2:.3f}")
>>> 0.667
```