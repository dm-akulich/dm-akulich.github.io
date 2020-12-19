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
-------
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
-------

```python
class Planet:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Planet {self.name}"


solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars", 
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
>>> [Planet Mercury, Planet Venus, Planet Earth, Planet Mars, Planet Jupiter, Planet Saturn, Planet Uranus, Planet Neptune]
```

# Атрибуты класса

```python
class Planet:
 
    count = 0 # атрибут класса
 
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1



earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)

>>> 2

mars.count

>>> 2
```

# Деструктор экземпляра класса

```python
class Human:

    def __del__(self):
        print("Goodbye!")


human = Human()
# в данном случае деструктор отработает - но все же 
# лучше создать метод и вызывать его явно
del human

>>> Goodbye!
```

# Словарь экземпляра и класса

```python
class Planet:
    """This class describes planets"""
    
    count = 1
    
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")
planet.__dict__ # покажет атрибуты экземпляра
>>> {'name': 'Earth', 'population': []}

planet.mass = 5.97e24
planet.__dict__ 
>>> {'mass': 5.97e+24, 'name': 'Earth', 'population': []}

Planet.__doc__
>>> 'This class describes planets'

print(dir(planet)) # покажет методы класса
>>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'mass', 'name', 'population']

planet.__class__ # покажет класс экземпляра
>>> __main__.Planet
```

# Работа с методами экземпляра

```python
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
 
    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)
>>> Welcome to Mars, Bob!

print(mars.population)
>>> [<__main__.Human object at 0x10e416780>]
```

# Вызов методов из методов

```python
class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age
 
    def _say(self, text): # приватный метод
        print(text)
 
    def say_name(self):
        self._say(f"Hello, I am {self._name}")
 
    def say_how_old(self):
        self._say(f"I am {self._age} years old")

bob = Human("Bob", age=29)

bob.say_name()
>>> Hello, I am Bob

bob.say_how_old()
>>> I am 29 years old
```

# Метод класса (@classmethod)
**Сlassmethod** - это встроенный объект, вам не нужно его ниоткуда импортировать, данный декоратор делает метод методом класса, в отличие от метода экземпляра, метод класса первым аргументом принимает не ссылку на конкретный экземпляр класса, а сам класс непосредственно, то есть в данном случае это будет класс **Event**, а не конкретный экземпляр. Внутри этого метода мы из пользовательского ввода, в данном случае это **user_input**, каким-то образом выделяем дату, которую пользователь хочет создать и описание события, на примере мы сделали это с помощью коротких функций-заглушек, которые из строки выделяют дату и описание.

```python
from datetime import date
class Event:
 
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"


event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_description, event_date)
print(event)
>>> Event "Рассказать, что такое @classmethod" at 2017-07-09
```
Получив описание и дату мы можем проинициализировать класс и вернуть экземпляр класса события на основе вот той строки, которую нам передал пользователь и получить экземпляр класса Event и как-то дальше с ним оперировать, добавить его в календарь. Таким образом **classmethod может быть полезен как например альтернативный конструктор вашего класса**. Давайте посмотрим, как им пользоваться. Когда после того как мы всё это объявили, у нас есть класс **Event** и мы можем вызвать метод класса **from_string** и передать в него строку. Произойдёт анализ этой строки и в результате нам вернётся экземпляр класса **Event** и мы видим, что у нас всё получилось, на экран вывелось как раз правильное описание события. Возможно вам сейчас не очень очевидно, зачем нужны класс-методы, но это становится более очевидным, когда появляется наследование. Класс-метод принимает на вход класс и этот класс будет всегда тем, который, внутри которого этот класс-метод описан и вы относительно этого класса можете не только его как-то инициализировать и вернуть, но вы также можете обращаться к атрибутам класса, делать всё что угодно, что вы можете сделать с классом. 

**Утверждения про classmethod:**
- Метод первым аргументом принимает класс
- К этому методу можно обращаться от экземпляра класса
- К этому методу можно обращаться от имени класса

```python
from datetime import date
def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class Event:
 
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date
    
    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)

event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")

print(event)
>>> 'Event "открытие чемпионата мира по футболу" at 2018-06-14'

print(event.__dict__)
>>> {'description': 'открытие чемпионата мира по футболу', 'date': datetime.date(2018, 6, 14)}
```

# Статический метод класса (@staticmethod)

Может так получиться, что вам нужно объявить **метод в контексте класса, но этот метод не оперирует ни ссылкой на конкретный экземпляр класса, ни самим классом непосредственно**, как мы видели в методе класса. В таком случае вам может помочь статический метод. 

**Утверждения про staticmethod:**
- Метод не принимает дополнительных аргументов кроме указанных программистом
- К этому методу можно обращаться от имени класса
- К этому методу можно обращаться от экземпляра класса

```python
class Human:
 
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

# можно обращаться от имени класса
Human.is_age_valid(35)
>>> True
```

Статический метод принимает только те аргументы, которые ему передают. Обратите внимание, что **здесь нет ни self, ни class аргументов**. В данном случае мы могли бы эту функцию объявить просто как обычную функцию, вне контекста класса, вне пространства имен класса. Но мы решили сделать это так, просто из соображений того, что этим будет удобнее пользоваться.

# Вычисляемые свойства класса (property)

```python
class Robot:

    def __init__(self, power):
        self.power = power

wall_e = Robot(100)
wall_e.power = 200
print(wall_e.power)
>>> 200
```
------

```python
class Robot:

    def __init__(self, power):
        self.power = power
    
    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power

wall_e = Robot(100)
wall_e.set_power(-20)
print(wall_e.power)
>>> 0
```
-------
## 1
```python
class Robot:
 
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power
    
    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power

wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)
>>> 0

del wall_e.power
>>> make robot useless
```

## 2
```python
class Robot:
    def __init__(self, power):
        self._power = power
    
    @property
    def power(self):
        # здесь могут быть любые полезные вычисления
        return self._power

wall_e = Robot(200)
wall_e.power
>>> 200
```

# Наследование и детализация реализации классов в Python












