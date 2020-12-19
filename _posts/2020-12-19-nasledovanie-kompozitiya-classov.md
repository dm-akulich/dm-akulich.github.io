---
layout: post
title: Классы и объекты, Наследование, Композиция классов в Python (Coursera. Погружение в Python)
comments: False
category: python
tags:
---

# Создание экземпляра (объекта) класса

```python
class Planet:
    pass

planet = Planet()

print(planet)

>>> <__main__.Planet object at 0x10e8722b0>
```

# Инициализация экземпляра

```python
class Planet:
    
    def __init__(self, name):
        self.name = name


earth = Planet("Earth")
print(earth.name)
print(earth)


>>> Earth
>>> <__main__.Planet object at 0x10e8796d8>

```

```python
class Planet:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


earth = Planet("Earth")
print(earth)

>>> Earth
```


```python
```

```python
```

```python
```
```python
```
```python
```
```python
```
```python
```


```python
```

<img src="/assets/img/2020-12-19-nasledovanie-kompozitiya-classov/1.png">