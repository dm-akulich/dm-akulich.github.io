---
layout: post
title: 'Паттерн ООП Singleton'
category: python
---

A singleton is a design pattern for creating only one instance of a class. Modules in Python are singletons by nature. A classic singleton checks whether the instance was created earlier; if not, it creates and returns it. The Borg singleton uses shared state for all objects. In the example shown in the chapter, we used the Singleton class for accessing a shared resource and a set of URLs to fetch images from, and both threads used it to properly parallelize their work.

Реализация на Python


```python
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


singleton = Singleton()
another_singleton = Singleton()
print(singleton is another_singleton)

>>> True
```