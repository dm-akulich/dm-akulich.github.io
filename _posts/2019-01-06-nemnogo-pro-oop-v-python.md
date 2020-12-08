---
layout: post
category: python
title: 'Немного про ООП в python'
---

# 1. Основы ООП

```python
class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age


vlad = Person()
vlad.name = "Vlad"
print(vlad.name, vlad.age)


ivan = Person()
ivan.age = 45
print(ivan.name, ivan.age)

katya = Person()
katya.set("Katia", str(21))
print(katya.name + " " + katya.age)
```

# 2. Наследование, инкапсуляция, полиморфизм

```python
############    Наследование.    ###########
# Наследование. Когда мы создаем еще один класс и он наследует все поля, методы родительского
class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1

igor = Student()
igor.set("Irog", 19)
print(" Имя:", igor.name, "; Возраст:",igor.age, "; Курс:", igor.course)

volodia = Student()
volodia.set("Volodia", 21)
volodia.course = 4
print(" Имя:", volodia.name, "; Возраст:",volodia.age, "; Курс:", volodia.course)

############    Инкапсуляция.    ###########
# Инкапсуляция. По сути это защита данных. Ограничение доступа к каким-либо полям или методам.
# Например, чтьобы какие-либо методы работали только в этом классе и ни в каком другом больше  
class Product:
    _price = 110
    color = "Red"

    def _set(self, price, color):
        self.price = price
        self.color = price


class Sneakers(Product):
    sneaker_size = 42

# Типа когда ставим ОДНО подчеркивание, то это говорит другим программистам, что не стоит использовать
# Этот метод, переменную вне этого класса или объекта. Но работать это будет все равно
# Если поставим два подчеркавания , то получится ошибка
class Animal:
    weight = 110
    color = "Grey"
    def __set(self, color):
        self.color = color


class Cat(Animal):
    eye_color = "Blue"

richi = Cat()
richi._Animal__set("Black")
print("Вес Ричи", richi.weight, "Цвет шерсти кота (защещенный метод)", richi.color)




#======== Полиморфизм ========
'''
Полиморфизм. Когда можем использовать один и тот же метод, но по разному в разных классах.
Например, функция print 
'''
print(2 + 2)
print('2' + '2')
```

# 3. Конструкторы в классах и переопределение методов

```python
'''
Конструктор - когда мы создаем какой-то объект, при объявдении объекта 
'''
class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

dima = Person("Dima", 22)
print(dima.name, dima.age)

'''
Переопределение методов
'''

class Animal:
    weight = 10
    def set(self, age, color):
        self.age = age
        self.color = grey

class Cat(Animal):
    def set(self, age, color, sex):
        self.age = age
        self.color = color
        self.sex = sex

richi = Cat()
richi.set(1, "orange", "male")
print(richi.age, richi.color, richi.sex)
```

# 4. Декораторы

```python
'''
Декораторы - обертки для функций. Когда у нас есть какая-либо функция и мы можем завернуть
ее в другую функцию. 
'''

def decorator(func):
    def wrapper():
        print("Код до выполения функции")
        func()
        print("Код который сработал после функции")
    return wrapper

@decorator
def show():
    print("Я обычная функция")

# show = decorator (show)
show()

```

## Дополнительно

Полезные функции:

- ```isinstance(имя_объекта, имяКласса)``` - является ли лбъект экземпляром классса
- ```issubclass(имяКлассаНаследника, имяСуперКласса)``` - является ли класс наследником другого класса


## Наcледование конструктора (```__init__```) при наследовании классов

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return f"Я - точка: координата x = {self.x}, координата y = {self.y}"

class Point3D(Point):
    def __init__(self, x, y, z):
        self.z = z
        Point.__init__(self, x, y) # наследуем конструктор
    def __repr__(self):
        return f"Я - 3D точка ({self.x}, {self.y}, {self.z})"

point = Point(10, 20)
point3d = Point3D(0, 0, 10)

print(point)
print(point3d)
```

Можно вместо строки ```Point.__init__(self, x, y)``` можно написать ```super().__init__(x,y)```.

```self``` - передается автоматически.

Все пользовательские атрибуты сохраняются в атрибуте ```__dict__```, который является словарем.

## Статические методы

**Статические методы в Python** – по-сути обычные функции, помещенные в класс для удобства и находящиеся в пространстве имен этого класса. Это может быть какой-то вспомогательный код. Вообще, если в теле метода не используется ```self```, то есть ссылка на конкретный объект, следует задуматься, чтобы сделать метод статическим. Если такой метод необходим только для обеспечения внутренних механизмов работы класса, то возможно его не только надо объявить статическим, но и скрыть от доступа из вне.

Для создания статических методов в Python предназначен декоратор ```@staticmethod```. У них нет обязательных параметров-ссылок вроде ```self```. Доступ к таким методам можно получить как из экземпляра класса, так и из самого класса:

```python
class SomeClass(object):
  @staticmethod
  def hello():
    print("Hello, world")

SomeClass.hello() # Hello, world
obj = SomeClass()
obj.hello() # Hello, world
```

Еще есть так называемые методы классов. Они аналогичны методам экземпляров, но выполняются не в контексте объекта, а в контексте самого класса  (классы – это тоже объекты). Такие методы создаются с помощью декоратора ```@classmethod``` и требуют обязательную ссылку на класс (```cls```).

```python
class SomeClass(object):
  @classmethod
  def hello(cls):
    print('Hello, класс {}'.format(cls.__name__))

SomeClass.hello() # Hello, класс SomeClass
```








