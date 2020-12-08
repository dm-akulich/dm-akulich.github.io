---
layout: post
title: 'Асинхронность в Python #3 Асинхронность на колбэках'
category: python
---

Теперь вместо select будем использовать модуль selectors.

Код для начала (это отредактированный немного код из предыдущего урока). С ним и будем работать

```python
import socket
import selectors

# Определяем дефолтный селектор системы
selectors = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)

def send_mesage(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        pass

if __name__ == "__main__":
    event_loop()
```

Модуль selectors выполняет тот же самый мониторинг над файлами, сокетами и всем другим, что имеет файловый дескриптор, что и функция select. Наша задача в отношении этого модуля остается той же самой что и в предыдущем уроке. Нужно мониторить объекты. И модулю selectors нужно сообщитьб что нас интересует. За кем следить и какое событие инетресует.

У модуля selectors есть метод ```.register()```. С помощью него зарегестрируем сокеты. ```.register()``` принимает три аргумента:

- файловый объект - объект у которого есть метод .fileno
- events - то событие, которое нас интересует (events=selectors.EVENT_READ)
- data - любые связанные данные (id сессии и тп) у нас это объект accept_connection. 

```python
import socket
import selectors

# Определяем дефолтный селектор системы
selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    # регаем серверный сокет

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        # регаем клиентский сокет
        selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_mesage)

def send_mesage(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        # прежде чем мы закрываем сокет, его нужно снять с регистрации.
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        pass

if __name__ == "__main__":
    event_loop()
```

## Теперь будем работать над ```event_loop()```

Первым делом нужно получить выборку объектов, которые готовы для чтения или для записи. Это будет переменная events, в которой используется метод ```.select()```.

Метод ```.select()``` возвращает кортеж, где первый элемент key, а второй элемент events. Events - это битовая маска события.

Первый элемент key - это объект SelectorKey, который является именованным кортежем (namedtuple). Этот именованный кортеж служит чтобы связать между собой сокет, ожидаемое событие и какие-то данные, соответствующие ему. По сути это контейнер. 

**Метод ```.select()``` у экземпляра класса ```selector``` возвращаяет список кортежей ```(key, event)```**. По одному кортежу на каждый зареганый объект. Распакуем их.


```python
import socket
import selectors

# Определяем дефолтный селектор системы
selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_mesage)

def send_mesage(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        # прежде чем мы закрываем сокет, его нужно снять с регистрации.
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        events = selector.select() # (key, events)

        #SelectorKey
        #fileobj
        #events
        #data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == "__main__":
    server()
    event_loop()
```

Все работает. После подключения к серверу двух клиентов все ОК.

















