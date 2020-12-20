---
layout: post
title: Дескрипторы (Crs. Погружение в Python)
comments: False
category: python
tags:
---

С помощью дескрипторов в Python реализована практически вся магия при работе с объектами, классами и методами. Чтобы определить свой собственный дескриптор, нужно определить класс. методы ```__get__```, ```__set__``` или ```__delete__```. После этого мы можем **создать какой-то новый класс и в атрибут этого класса записать объект типа дескриптор**. Таким образом, наш атрибут будет являться дескриптором. Что это значит? У него будет переопределено поведение при доступе к атрибуту, при присваивании значений или при удалении. 

```python
# descriptor.py
class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')
    
    def __set__(self, obj, value):
        print('set')
    
    def __delete__(self, obj):
        print('delete')
        
class Class:
    attr = Descriptor()


instance = Class() 
```

Метод ```__get__``` определяет поведение при доступе к атрибуту. Метод ```__set__``` будет переопределять какое-то поведение, если мы попытаемся в наш атрибут что-то присвоить, а метод ```__delete__``` будет говорить о том, что будет происходить, если мы удалим наш атрибут. Мы создадим объект класса Class и посмотрим, что будет происходить при обращении к атрибуту. Если мы просто попытаемся вывести наш атрибут, у нас вызовется метод ```__get__```. Если мы запишем в него какое-то значение, у нас вызывается метод ```__set__```. А если мы его удаляем, вызывается метод ```__delete__```. 


```python
# descriptor.py продолжение
print(instance.attr)
>>> 'get'

instance.attr = 10
>>> 'set'

del instance.attr
>>> 'delete'
```

Например, мы можем определить дескриптор **Value**, который будет переопределять поведение при присваивании значения в него. Мы определим наш класс с атрибутом, который будет являться дескриптором, и при присваивании значений в дескриптор у нас будет происходить модифицированное поведение. То есть наш метод ```__set__``` говорит о том, что, когда мы присваиваем значение в наш дескриптор, мы не просто сохраняем это значение, но мы как-то его препроцессим. В данном случае просто умножаем на десять. Таким образом, когда мы присваиваем десятку в наш атрибут, который является дескриптором, у нас, на самом деле, сохраняется сотня. ```__get__``` и ```__set__```. Этого уже достаточно для того, чтобы наш класс являлся дескриптором. Вы можете переопределить любой из трех методов, и класс уже будет являться дескриптором. Если у вас переопределен только метод ```__get__```, то это non-data дескриптор, если ```__set__``` или delete — то это data дескриптор. Это говорит о том, в каком порядке они будут искаться, вызываться при поиске атрибутов. **(пример ниже)**

```python
# another_descriptor.py
class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class:
    attr = Value()


instance = Class()
instance.attr = 10

print(instance.attr)
>>> 100
```

### Задача: написать свой дескриптор

Который пишет в файл все присваиваемые ему значения.

```python
class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'a') as f:
            f.write(str(value)+'\n')

            self.amount = value


class Account:
    amount = ImportantValue(100)


bobs_account = Account()
bobs_account.amount = 150
bobs_account.amount = 200

with open('log.txt', 'r') as f:
    print(f.read())
>>> 150
>>> 200
```

### Задача. Свой дескриптор

```python
# Descriptor with commission
class Value:
    def __init__(self):
        self.amount = 0

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value - value * obj.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)
>>> 90
```