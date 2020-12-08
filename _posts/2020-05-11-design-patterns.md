---
layout: post
category: python
title: 'Принципы и паттерны проектирования Python'
---

# 1. SOLID принципы

# 2. Паттерны проектирования

Классификация паттернов проектирования:

- **Структурные шабоны** - модифицируют структуру объектов, они могу служить для получения из классов более сложных структур
- **Порождающие шабоны** - используются при создании различных объектов. Признаны разделить процесс создания объекта и использование их системой.
- **Поведенческие шабоны** - описывают способы реализации взаимодействия между объектами различных типов.

## 2.1 Порождающие паттерны проектирования

### 2.1.1 Фабричный метод

**Фабричный метод** - общий интерфейс создания экземпляров подклассов некоторого класса.

### 2.1.2 Абстрактная фабрика (Abstract Factory)

**Абстрактная фабрика** - создание семейств взаимосвязанных объектов. Для программы не имеет значение, как создаются компоненты. Необходима ли "фабрика", производящая компоненты, умеющие взаимодействовать друг с другом.

### 2.1.3 Строитель

**Строитель** - сокрытие инициализации для сложного объекта.

### 2.1.4 Прототип (Prototype)

### 2.1.5 Одиночка (Singleton)

## 2.2 Структурные паттерны
### 2.2.1 Адаптер (Adapter)

**Адаптер** - взаимодействие несовместимых объектов.

Задача паттерна: русть есть некоторый объект и система, с котоорой этот объект должен взаимодействовать, при этом интерфейс объекта не может быть напрямую встроен в систему. В таком случае и используется паттерн **Адаптер**.

<img src="/assets/img/2020-05-11-design-patterns/adapter-1.png">

Он позволяет создать объект, который может обеспечить взаимодействие нашего исходного объекта с системой.

<img src="/assets/img/2020-05-11-design-patterns/adapter-2.png">

**Реализация на Python**

**Задача**: пусть есть некотоорая система, которая берет какой-то текст, делает его предварительную обработку, а дальше хочет вывести в порядке убывания их частоты, но собственного обработчика у системы нет. Она принимает в качетсве обработчика некоторый объект, который имеет свой слабый интерфейс. В качесвте обработчика у нас есть некоторый счетчик слов, который может по заданному тексту посчитать слова, может сказать сколько раз встретилось конкретное слово, а также может вывести частотный словарь всех встреченных слов. 


```python
import re
from abc import ABC, abstractmethod

class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp
    
    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')

class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass

# Обработчик
class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)
    
    def get_all_words(self):
        return self.__words.copy()

# сделаем объект системы и передадим в него некоторый текст
text = 'Design Patterns: Elements of Reusable Object-Oriented Software (1994) is a software engineering book describing software design patterns. The book was written by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, with a foreword by Grady Booch. The book is divided into two parts, with the first two chapters exploring the capabilities and pitfalls of object-oriented programming, and the remaining chapters describing 23 classic software design patterns. The book includes examples in C++ and Smalltalk.'

# Передали тест системе 
system = System(text)
print(system.text)

# Создадим обработчик
counter = WordCounter()

# Попробуем передать наш обработчик системе
# system.get_processed_text(counter)

# И вылетает ошибка
# "AttributeError: 'WordCounter' object has no attribute 'process_text'"
# Потому что интерфейсы обработчика и системы несовместимы

# Напишем адаптер, который позволит использовать обработчик в системе

class WordCounterAdapter(TextProcessor):
    # Конструктор в качестве второго аргумента будет принимать некоторый объект,
    # который мы хотим адаптировать и схранять в некоторую переменную класса
    def __init__(self, adaptee):
        self.adaptee = adaptee

    # напишем метод, который будет принимать на вход текст,
    # а возвращать слова в порядке убывания их частоты встреч
    def process_text(self, text):
        self.adaptee.count_words(text)
        # чтобы получить из словаря список всех слов, используем метод keys
        words = self.adaptee.get_all_words().keys()
        # Необходимо вернуть отсортированыый массив слов
        return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse = True)


adapter = WordCounterAdapter(counter)
system.get_processed_text(adapter)
```


### 2.2.2 Мост (Bridge)

**Мост** - разделение абстракции и реализации


### 2.2.3 Компоновщик

**Компоновщик** - агрегирование нескольких объектов в одну структуру.

### 2.2.4 Декоратор (Decorator)

**Декоратор** - динамическое создание дополнительного поведения объекта.

Задача паттерна **Декоратор**: позволяет динаимчески добавлять некоторому объекту функциональность, которой у него до этого не было. Реализуется этот паттерн путем создания **абстрактного базового Класса**, **Абстрактного декоратора для этого класса** и их наследников: базовых классов и базовых декораторов.

<img src="/assets/img/2020-05-11-design-patterns/decorator.png">

Применение декоратора к объекту заключается в оборачивании объекта в декоратор с некоторой функциональностью. К этому объекту может быть применено несколько декораторов.

<img src="/assets/img/2020-05-11-design-patterns/decorator-2.png">

**Реализация на Python**

Пример задачи: создать мир с животными: некотоыре бегают быстро, некоторые бегают медленно, множество видов. Вместо того, чтобы описывать каждый вид, решили сделать декоратор

```python
from abc import ABC, abstractmethod

class Creature(ABC):
    
    @abstractmethod
    def feed(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass

class Animal(Creature):
    def feed(self):
        print('I eat grass')

    def move(self):
        print('I walk forward')

    def make_noise(self):
        print('WOOO!')

# Начнем создавать иерархию декораторов
# Для начала опишем абстрактный декоратор, от которого будут наследоваться все остальные

class AbstractDecorator(Creature):
    '''
    В этом классе необходимо реализовать init, в котором будем хранить наш базовый объекь для декоратора
    '''
    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()
        
    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()

# теперь сделаем Конкретный декоратор, например, водоплавающее животное

class Swimming(AbstractDecorator):
    '''
    В этом классе изменим метод move() и make_noise().
    '''

    def move(self):
        print('I swim forward')

    def make_noise(self):
        print('...')

## Сделваем еще два декоратора: хищник и быстрое животное

class Predator(AbstractDecorator):
    def feed(self):
        print('I eat other animals')

class Fast(AbstractDecorator):
    def move(self):
        self.base.move()
        print('Fast')

## Попробуем применить декораторы

animal = Animal() # это стандартное животное, которое ест страву, ходит и кричит ВУУУ!
# print(animal.make_noise())
# print(animal.move())
# print(animal.feed())

# Сделаем водоплавающее животное

swimming = Swimming(animal)
# print(swimming.move())
# print(swimming.make_noise())

# Сделаем хищника водоплавающего
predator = Predator(swimming)

# сделаем его еще быстрым

fast = Fast(predator)

# сделаем его еще быстрее

faster = Fast(fast)

# Снятие декораторов
```

## 2.3 Поведенческие паттерны

### 2.3.1 Наблюдатель (Observer)

**Наблюдатель** - Оповещение об изменении некоторого объекта 

Задача паттерна **Наблюдатель**: пусть в некоторой системе есть наблюдаемый объек, который со временем изменяет свое состояние и объект наблюдатель, который отслеживает состояние некоторого объекта. Наблюдатель хочет своевременно узнавать об измененяих в наблюдаемом объекте. В целом задача паттерна в том, чтобы наблюдаемый объект оповещал наблюдателей об изменении.

<img src="/assets/img/2020-05-11-design-patterns/observer-1.png">

**Реализация на Python**: Пусть у нас есть какой-то менежджер уведомлений, который может рассылать уведомления по подписчикам, и есть подписчики этого менеджера.

Подписчиков есть два типа:

- принтер, который печатает сообщения, который посылаем менеджер
- и нотифаер, который просто сообщает о том, что уведомление пришло.

```python
from abc import ABC, abstractmethod

# Создадим класс менеджер уведомлений
class NotificationManager:
    # у него в инициализаторе объявим пустой список с подписчиками
    def __init__(self):
        self.__subscribers = set()
    
    # для того, чтобы подписчик мог подписаться на уведомления 
    # менеджера, добавим методы subscribe и unsubscribe

    def subscribe(self, subscriber):
        # subscribe добавляет нашего подписчика в __subscribers
        self.__subscribers.add(subscriber)
    
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
    
    # Важной частью наблюдателя является собственно отправка уведомлений,
    # для этого сделаем метод notify, который должен отправить
    # уведомление всем подписчикам. 

    def notify(self, message):
        # Чтобы отправить уведомления подписчикам,
        # необходимо вызвать у них метод update.
        for subscriber in self.__subscribers:
            subscriber.update(message)

# Объявим абстрактного наблюдателя
class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Объявим две конкретные реализации Нотифаера и Принтера
class MessageNotifier(AbstractObserver):
    # В инициализаторе дадим ему некоторое имя.
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} received message!")

class MessagePrinter(AbstractObserver):
    # В инициализаторе дадим ему некоторое имя.
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} received message: {message}")

# Создадим один нотифаер и два принтера
notifier = MessageNotifier("Notifier 1")

printer1 = MessagePrinter("Printer 1")
printer2 = MessagePrinter("Printer 2")

# Объявим менеджер уведомлений

manager = NotificationManager()

# Подпишем наших наблюдателей к нашему менеджеру

manager.subscribe(notifier)
manager.subscribe(printer1)
manager.subscribe(printer2)

# Попробуем отправить им какое-нибудь сообщение

manager.notify("Hi ")
```

### 2.3.2 Цепочка обязанностей (Chain of Responsibility)

**Цепочка обязанностей** - обработка данных несколькими объектами.

Некоторому классу задается список зданий, посче чего производится запуск сразу всех действий.

<img src="/assets/img/2020-05-11-design-patterns/chain-1.png">

**Ключевое свойство Цепочки Обязанностей: Обработай сам или передай другому**.

Использование: 

### 2.3.3 Команда

**Команда** - 

### 2.3.4 Итератор (Iterator)

**Итератор** - 

### 2.3.5 Посредник

**Посредник** - 

### 2.3.6 Интерпретатор

**Интерпретатор** - 

### 2.3.7 Стратегия (Strategy)

**Стратегия** - выбор из нескольких вариантов поведения объекта.

