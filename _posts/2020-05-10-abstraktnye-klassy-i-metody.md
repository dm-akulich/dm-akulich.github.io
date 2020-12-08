---
layout: post
category: python
title: 'Абстрактные классы и методы'
---

**Абстрактным классом** называется класс, который предназначен, чтобы его расширять. Абстрактный класс не предназначен для создания объектов. Описывает абстрактную логику.

В python есть еще абстрактные методы - **абстрактные методы** - методы без реализации.

```python
import abc

class AbstractServer(abc.ABC):
    def __init__(self, version):
        self.version = version
    
    @abc.abstractmethod
    def connect(self):
        pass

class ServerApache(AbstractServer):
    def connect(self):
        print('Connection from Apache')
```

Если в классе-наследнике не будет описан метод connect, то будет ошибка.

Обычно под интерфесом понимается абстрактный класс с абстрактными методами. Интерфейс это как-бы то, что должно быть в классе наследнике.



