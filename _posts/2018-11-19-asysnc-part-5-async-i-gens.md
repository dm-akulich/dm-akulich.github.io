---
layout: post
title: 'Асинхронность в Python #5 Асинхронность на генераторах'
category: python
---

Асинхронность на генераторах

# Исходный код

```python
import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept() #read
        print('Connection from', addr)
        client(client_socket)

def client():
    while True:
        print('Before recv()')
        request = client_socket.recv(4096) #read
        
        if not request:
            break
        else:
            response = 'Hello World\n'.encode() #write
            client_socket.send(response)
    
    print('Outside the inner while')
    client_socket.close()

server()
client()
```

Задача сейчас состоит в том, чтобы определить какие сокеты готовы и вызвать у них соответствующие методы: ```.accept()```, ```.recv()```, ```.send()```.

Еще нам нужен механизм, который мог бы переключать управление между фунцкиями ```server``` и ```client```.

```python
import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:

        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() #read

        print('Connection from', addr)
        client(client_socket)

def client():
    yield server_socket
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4096) #read
        
        if not request:
            break
        else:
            response = 'Hello World\n'.encode() #write
            yield ('write', client_socket)
            client_socket.send(response)
    
    print('Outside the inner while')
    client_socket.close()

server()
client()
```

Так как мы использовали функцию select, куда мы будем передавать сокеты, то эти сокеты мы связываем с функциями генераторами. 

Когда выполнение функции доходит до блокирующей операции, он прежде отдает кортеж с сокетом.

**Пишем событийный цикл**

Сделали список с задачами ```tasks = []```, откуда потом будем брать первый элемент и что-то потом с ним делать.

В цикле ```while``` использовали функцию ```any()```, которая принимает на вход список значений, каждое из которых возвращает ```True``` или ```False```. Если хоть один из них будет ```True```, то ```any``` вернет ```True```.

```while any([tasks, to_read, to_write])``` - Если словать ```to_read``` пустой, он интерпретируется как ```false```. То же и про другие.


```python
import socket
from select import select
# задачи добавили 
tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:

        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() #read

        print('Connection from', addr)
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096) #read
        
        if not request:
            break
        else:
            response = 'Hello World\n'.encode() #write
            yield ('write', client_socket)
            client_socket.send(response)
    
    client_socket.close()

def event_loop():
    print('before any()')

    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
        	# тут происходит получение генератора 
            task = tasks.pop(0)

            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            
            if reason == 'write':
                to_write[sock] = task
        
        except StopIteration:
            print('Done')



tasks.append(server())
event_loop()
```

И все работает.











