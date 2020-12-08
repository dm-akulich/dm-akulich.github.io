---
layout: post
title: 'Асинхронность в Python #2 Асинхронность с простыми функциями. Событийный цикл'
category: python
---

Тут будет про простой событийный цикл.

Работаем с этим.

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Before accept()')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        print('Before recv()')
        request = client_socket.recv(4096)
        
        if not request:
            break
        else:
            response = 'Hello World\n'.encode()
            client_socket.send(response)
    
    print('Outside the inner while')
    client_socket.close()
```

Немного отредачим это (закинем по функциям)

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        print('Before accept()')
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        send_mesage(client_socket) # это потом уберем, чтобы "разорвать связность между функциями"

def send_mesage(client_socket):
    while True:
        print('Before recv()')
        request = client_socket.recv(4096)
        
        if not request:
            break
        else:
            response = 'Hello World\n'.encode()
            client_socket.send(response)
    
    client_socket.close()

if __name__ == "__main__":
    accept_connection(server_socket)
```

Этот код работает так же как и предыдущий. Он выполняется последовательно.

Необходимо функции send_connection и send_message сделать как бы независимыми. Чтобы мы могли их вызвать когда захотим, то есть уменишить их связанность.

В данном случае нужно сделать этот самый механизм переключения упарвления (функция event loop).

*Примечание: функция select, это системная функция, которая нужна для мониторинга изменений состояний файловых объектов сокетов*

Когда, например, мы вызываем метод bind, создается файл с точки зрения системы.

Функция select работает с любым объектом, у которого есть метод .fileno(). Этот метод возвращает файловый дескриптор (целое число, которое ассоциируется с конкретным файлом в файловой системе). Функция select мониторит изменение тех файловых объектов, которые мы в нее передали. На вход функция select получает три списка с файловыми дескрипторами или с объектами, у которых есть метод .fileno(). Эти списки как раз те самые объекты, за изменением состояния которых нужно следить.

- Первый список - те объекты, за которыми нужно наблюдать, когда они станут доступны для **чтения**
- Второй список - те объекты, за которыми нужно наблюдать, когда они станут доступны для **записи**
- Третий список - те объекты, от которых мы ожидаем **ошибок** 

Функция select принимает вот эти три списка и в результате возвращает эти же три списка, но возвращает их после того, как они станут доступны для чтения, для записи, и третий список - объекты с ошибками

Пояснение под кодом.

```python
import socket
from select import select

# Список с сокетами, который нужно мониторить когда они станут доступны для чтения 
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        to_monitor.append(client_socket)

def send_mesage(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], []) # read, write, errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_mesage(sock)


if __name__ == "__main__":
    to_monitor.append(server_socket)
    event_loop()
```

```to_monitor``` - Список с сокетами, который нужно мониторить когда они станут доступны для чтения. Этот список мы передаем в качестве первого аргумента в функцию ```select```. Как только пользователь что-то напишет, select создает список с объектами, которые готовы для чтения. Все это мы распаковывем в список ```ready_to_read```.

Как только пояявялется спискок с объектами, мы его определеннм образом обрабатываем. Сделаем это циклом ```for```.

Теперь все работает и серверный сокет может обслуживать два клиента.




































