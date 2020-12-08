---
layout: post
title: 'Паттерны ООП Abstract Factory'
category: python
---


<img src="/assets/img/2020-05-31-patterns-abstract-factory/abstract-factory.png">
<img src="/assets/img/2020-05-31-patterns-abstract-factory/abstract-factory-2.png">




Пример: у нас есть две фабрики и над ними мы делаем абстрактную фабрику. Всего три файла

1. **Chair Factory**

```python
# chair_factory.py

from abc import abstractmethod, ABC


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
    print(CHAIR.get_dimensions(), CHAIR.__class__)
    CHAIR2 = ChairFactory.get_chair("MediumChair")
    print(CHAIR2.get_dimensions(), CHAIR2.__class__)
    CHAIR3 = ChairFactory.get_chair("SmallChair")
    print(CHAIR3.get_dimensions(), CHAIR3.__class__)

```

2. **Table Factory**

```python
# table_factory.py

from abc import abstractmethod, ABC


class InterfaceTable(ABC):

    @abstractmethod
    def get_dimensions(self):
        """The Chair Interface"""
        pass


class BigTable(InterfaceTable):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumTable(InterfaceTable):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallTable(InterfaceTable):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class TableFactory():

    @staticmethod
    def get_chair(table_type):
        try:
            if table_type == 'BigTable':
                return BigTable()
            elif table_type == 'MediumTable':
                return MediumTable()
            elif table_type == 'SmallTable':
                return SmallTable()
            else:
                raise AssertionError("Table not found")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    TABLE = TableFactory.get_chair("BigTable")
    print(TABLE.get_dimensions(), TABLE.__class__)
    TABLE2 = TableFactory.get_chair("MediumTable")
    print(TABLE2.get_dimensions(), TABLE2.__class__)
    TABLE3 = TableFactory.get_chair("SmallTable")
    print(TABLE3.get_dimensions(), TABLE3.__class__)

```

3. **Furniture Abstract Factory**

```python
# furniture_abstract_factory.py

from abc import ABC, abstractmethod
from chair_factory import ChairFactory
from table_factory import TableFactory


class InterfaceFurnitureFactory(ABC):

    @abstractmethod
    def get_furniture(furniture_type):
        """ The static furniture interface method """
        pass


class FurnitureFactory(InterfaceFurnitureFactory):

    @staticmethod
    def get_furniture(furniture_type):
        try:
            if furniture_type in ["BigChair", "MediumChair", "SmallChair"]:
                return ChairFactory.get_chair(furniture_type)
            elif furniture_type in ["BigTable", "MediumTable", "SmallTable"]:
                return TableFactory.get_chair(furniture_type)
            raise AssertionError("Cannot find furniture type")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    FURNITURE = FurnitureFactory.get_furniture("SmallChair")
    print(FURNITURE.__class__, FURNITURE.get_dimensions())

    FURNITURE2 = FurnitureFactory.get_furniture("BigChair")
    print(FURNITURE2.__class__, FURNITURE2.get_dimensions())

    FURNITURE3 = FurnitureFactory.get_furniture("BigTable")
    print(FURNITURE3.__class__, FURNITURE3.get_dimensions())

```

**Вывод следующий**

```python
>>> <class 'chair_factory.SmallChair'> {'height': 60, 'width': 60, 'depth': 60}
>>> <class 'chair_factory.BigChair'> {'height': 80, 'width': 80, 'depth': 80}
>>> <class 'table_factory.BigTable'> {'height': 80, 'width': 80, 'depth': 80}
```