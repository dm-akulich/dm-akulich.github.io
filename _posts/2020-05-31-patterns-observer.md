---
layout: post
title: 'Паттерн ООП Observer'
category: python
---

# Паттерн ООП Наблюдатель (Observer)


Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

<img src="/assets/img/2020-05-31-patterns-observer/observer.png">

```python
# pattern_oop_observer.py

class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Observer:
    def update(self, *args, **kwargs):
        pass


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("American stock market received: {0}\n{1}".format(args, kwargs))


class EuropeanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("European stock market received: {0}\n{1}".format(args, kwargs))


if __name__ == "__main__":
    really_big_company = Observable()

    american_observer = AmericanStockMarket()
    really_big_company.register(american_observer)

    european_observer = EuropeanStockMarket()
    really_big_company.register(european_observer)

    really_big_company.update_observers('important update', msg="CEO unexpectedly resigns")

```

**OUTPUT**

```python
>>> American stock market received: ('important update',)
>>> {'msg': 'CEO unexpectedly resigns'}
>>> European stock market received: ('important update',)
>>> {'msg': 'CEO unexpectedly resigns'}
```











