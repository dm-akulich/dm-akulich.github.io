---
layout: post
title: 'Паттерны ООП Factory'
category: python
---


Factory is a class for creating other objects. Usually this class has methods that accept some parameters and returns some type of object depending on the parameters passed.

- Factories provide loose coupling, separating object creation from using specific class implementation.
- A class that uses the created object does not need to know exactly which class is created. All it needs to know is the created class' interface, that is, which created class' methods can be called and with which arguments. Adding
new classes is done only in factories as long as the new classes comply with the interface, without modifying the client code.
- The Factory class can reuse existing objects, while direct instantiation always creates a new object.

<img src="/assets/img/2020-05-31-patterns-building-factories/factory.png">

Пример простой фабрики

```python
class SimpleFactory(object):
    @staticmethod  # This decorator allows to run method without
    # class instance, .e. SimpleFactory.build_connection
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol == 'ftp':
            return FTPConnection()
        else:
            raise RuntimeError('Unknown protocol')


if __name__ == '__main__':
    protocol = raw_input('Which Protocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print(protocol.get_response())
```

Пример реализации фабричного метода

```python
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        Обратите внимание, что Создатель может также обеспечить реализацию
        фабричного метода по умолчанию.
        """
        pass

    def some_operation(self) -> str:
        """
        Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """

        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
результирующего продукта.
"""


class ConcreteCreator1(Creator):
    """
    Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


class Product(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())


>>> App: Launched with the ConcreteCreator1.
>>> Client: I'm not aware of the creator's class, but it still works.
>>> Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}

>>> App: Launched with the ConcreteCreator2.
>>> Client: I'm not aware of the creator's class, but it still works.
>>>> Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
```

**Еще хороший пример фабрики (самый хороший пример)**

```python
from abc import ABCMeta, abstractstaticmethod, abstractmethod, ABC


class InterfaceChair(ABC):

    @abstractmethod
    def get_dimensions(self):
        """The Chair Interface"""
        pass


class BigChair(InterfaceChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumChair(InterfaceChair):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallChair(InterfaceChair):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory():

    @staticmethod
    def get_chair(chair_type):
        try:
            if chair_type == 'BigChair':
                return BigChair()
            elif chair_type == 'MediumChair':
                return MediumChair()
            elif chair_type == 'SmallChair':
                return SmallChair()
            else:
                raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    CHAIR = ChairFactory.get_chair("BigChair")
    print(CHAIR.get_dimensions())
    CHAIR2 = ChairFactory.get_chair("MediumChair")
    print(CHAIR2.get_dimensions())
    CHAIR3 = ChairFactory.get_chair("SmallChair")
    print(CHAIR3.get_dimensions())


>>> {'height': 80, 'width': 80, 'depth': 80}
>>> {'height': 70, 'width': 70, 'depth': 70}
>>> {'height': 60, 'width': 60, 'depth': 60}

```