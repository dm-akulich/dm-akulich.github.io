---
layout: post
category: python
title: 'Структуры данных в Python'
---

**Структуры данных** - способ организации информации в памяти компьютера.

Зачем это может пригодиться:

- Хранить реальные данные
- Как вспомогательный инструмент
- Для моделирования

## 1. Массив

**Массив** - данные которые хранятся последовательно. Классический массив как правило содержит данные одного типа. Еще идеальный массив должен быть фиксированной длины. И **исспользуем его, когда нам нужен точечный доступ к элементу**. Сложность: **O(1)**. 

<img src="/assets/img/2020-05-10-data-strukture-python/massiv-1.png">

<img src="/assets/img/2020-05-10-data-strukture-python/massiv-2.png">

## 2. Список (официальное название Связный список)

Суть в том, что каждый элемент имеет ссылку на последующий элемент, список может храниться в любом месте в Python, но порядок нужно сохранять.

<img src="/assets/img/2020-05-10-data-strukture-python/svyaz-spisok.png">

<img src="/assets/img/2020-05-10-data-strukture-python/svyaz-spisok-2.png">

Тут уже есть проблема с точечным доступок к элементу.

<img src="/assets/img/2020-05-10-data-strukture-python/svyaz-spisok-3.png">

<img src="/assets/img/2020-05-10-data-strukture-python/svyaz-spisok-4.png">

У узла должны быть как минимум **две составляющие: значение и ссылка на следующий узел**.

**Реализация списка на Python**

```python
# List()
# add(item) - добавляет в левую часть
# remove(item)
# search(item) -> True/False
# is_empty() пустой или не пустой список
# size()
# append(item) -  добавляет в правую часть
# index(item) - возвращает индекс элемента
# insert(position, item) - вставляет на позицию
# pop()
# pop(position)

class Node(): # узел
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data

    def set_next(self, node):
        self.__next = node
    
    def get_next(self):
        return self.__next


class LinkedList():
    def __init__(self):
        self.__head = None
    
    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)
        self.__head = node

    def size(self):
        current = self.__head
        counter = 0
        while not current is None:
            current = current.get_next()
            counter += 1
        return counter

my_list = LinkedList()
my_list.add(42)
my_list.add(33)
my_list.add(17)

print(my_list.is_empty())
print(my_list.size())
```


## 3. Абстрактные структуры данных: **Стек**

**Стек** - упорядоченная коллекция элементов. Как правило, добавление или удаление элментов происходит на одном из концов (вершине стека). 

В стеке LIFO (last-in-first-out). Доступ мы имеет только к последнему добавленному элементу.

<img src="/assets/img/2020-05-10-data-strukture-python/stek-1.png">

По факту рекурсия использует принцип стека.

<img src="/assets/img/2020-05-10-data-strukture-python/stek-2.png">

У стека есть несколько стандартных метода:

- ```push(item)``` - вставляем элемент
- ```pop(item)``` - достаем элемент
- ```peek(item)``` - посмотреть что на топе стека, но не доставать
- ```is_empty()``` - пустой ли стек
- ```size()``` - какой размер стека

Пример: проверка палиндрома

```python
def is_palindrome(word):
    word = word.lower()
    rword = ""

    stack = Stack()

    for char in word:
        stack.push(char)

    while not stack.is_empty():
        rword += stack.pop()
    
    return word == rword
```

Опишем стек на python

```python
class Stack():
    def __init__(self):
        self.__data = list()
    
    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        else:
            return None
    
    def peek(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        else:
            return None

    def is_empty(self):
        return len(self.__data) == 0
    
    def size(self):
        return len(self.__data)
```

## 4. Абстрактные структуры данных: **Очередь**

**Очередь (Queue)** - очень похожа на стек. FIFO (First-In-First-Out).

В стеке мы:
- можем извлекать элемент в начале 
- можем вставлять элемент в конец
- можем подсмотреть элементы в начале и в конце


<img src="/assets/img/2020-05-10-data-strukture-python/ochered-1.png">

```python
class Queue():
    def __init__(self):
        self.__data = list()
    
    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        else:
            return None
    
    def rear(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        else:
            return None
    
    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        else:
            return None

    def is_empty(self):
        return len(self.__data) == 0
    
    def size(self):
        return len(self.__data)
    
    def clear(self):
        self.__data = list()

    def show(self):
        print('\n'.join(str(val) for val in self.__data))
```











