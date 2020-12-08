---
layout: post
title: 'Асинхронность в Python #0 Веб приложение на низком уровне'
category: python
---

Тут речь пойдет про сокеты, ip, tcp.

Задача состоит в том, что нам нужно обработать запрос пользователя. Выяснить, что он хочет сделать, какие методы он используем и по какому маршруту направляется. И в зависимости от этого мы должны сгенерировать ему ответ.

Работать будем с  протоколом HTTP. Протокол http в свою очередь базируется на двух протоколах: TCP и IP.

### Протокол IP

Протокол IP тут с самым низким уровнем абстракции. Сверху над ним находится TCP (он более абстрактный). И с самым высоким уровнем абстракции HTTP.
Особенность протокола IP в том, что между двумя хостами(двумя машинами) создается тоннель передачи данных, данные передаются пакетами. Проблема в том, что эти пакеты могут потеряться по дороге, повредиться и тп. Основаня часть IP протокола - это IP-адрес. 

### Протокол TCP

Так как IP протокол не cовсем надежный, был разработан специальный транспрортный протокол на транспортном уровне TCP (Transmission Control Protocol), который отвечает именно за доставку по протоколу IP. Он следит за тем, чтобы соблюдался порядок получения данных и отправки пакетов, Если каки-то пакетов не хватает, он делает повторный запрос, убирает дубли. Его особенность в том, что он привносит в конструкцию данных порт port:XXXX. Порты нужны для того, чтобы несколько приложений могли использовать TCP на одной машине, не занимая собой весь туннель.

*Типа IP-address - это жилой дом, а TCP-порты - это квартиры, где за каждой квартирой (открытым портом) своя служба, которая обслуживает запрос клиента (server)*

### Сокеты

И эта пара ip-address:8000 - это сокет (с англа переводится как гнездо). Это типа мостик между кем-то и кем-то, между отправителем и получателем. 

Сокеты быват двух видов:

- Серверные
- Клиентские

На примере python

Для того, чтобы установить соединение между двумя хостами по протоколу TCP/IP (HTTP), импортируем модули и тп.

Задача в том, что нужно установить соединение между клиентом и сервером. Клиент - это тот, кто принимает запрос, сервер это тот, кто запрос обрабатывает.


Первым делом создадим субъекта, что будет принимать запрос. Это будет переменная server_socket, в ней будет вызываться метод socket, которому необходимо передать аргументы.

Тк подключение будет по протоколу IP/TCP, то укажем это: socket.AF_INET - это глобальная переменная, AF (Adress Family), а INET - сам протокол IP, который может быть двух версий, 4-я (IPv6) и 6-я версия. INET это протокол 4-й версии. Если нужна 6-я версия, то это будет AF_INET6. 4-я версия это стандартный протокол из четырех частей, разделенных точками по одному байту на часть.

Вторым аргументом передаем TCP - это глобальная переменная SOCK_STREAM. Субъект создан и мы указали протоколы, которые это субъект будет использовать и ожидать получения пакетов по этим протоколам.

```python

import socket

def run():
	  # созданный субъект
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == "__main__":
    run()
```

Следующим шагом свяжем этого субъекта с конкретный адресом и конкретным портом.

```python
import socket

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # связали
    server_socket.bind(('localhost'), 5000)

if __name__ == "__main__":
    run()
```

Теперь сокет должен ждать обращения по этому адресу и на этот порт.

Теперь необходимо сделать так, чтобы сокет начал прослушивать этот адрес и этот порт.

```python
import socket

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    # дали указание на прослушивание пакетов
    server_socket.listen()

if __name__ == "__main__":
    run()
```

Порт слушает на наличие входящих пакетов.

Так как отношения между сервером и клиентом длящиеся, то нам нужно постоянно получать от клиента данные и постоянно как-то на них реагировать, потому что мы не знаем какие это данные и насколько сессия будет длинная, то используем бесконечный цикл.


```python
import socket

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()
    # добавили цикл
    while True:
 ```

Допустим, клиент сделал запрос на сервер и серверный сокет получил ответ, и нам нужно посмотреть ответ

```python
def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()

    while True:
    	  # за просмотр отвечает метод accept, эта строка говорит о том, что сервер что-то принял
        server_socket.accept()
```

Метод accept возвращает кортеж, распакуем этот кортеж по переменным и посмотрим, что там получается. Первый элемент кортежа это сокет, а второй элемент это адрес.

```python
def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
```

accept возвращает нам клиентский сокет.

На данный момент мы уже описали серверый сокет 

```python
def run():
	  # серверный сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()

    while True:
    	  # клиентский сокет
        client_socket, addr = server_socket.accept()
```

Теперь, поскольку клиент сделал какой-то запрос, хорошо бы его увидеть, созраним его в переменую request, которая будет принимать значение ```request = client_socket.recv(1024)```, где recv - receive, а 1024 - количество байт в пакете. И выведем это на печать.

```python
def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        # запрос клиента
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)
```

Теперь нужно ответить клиенту. Так как сокеты не принимают строки, то строку необходимо перекодировать в байты методом **encode()**. Метод encode возвращает тип данных bytes. 

Чтобы увидеть в бразуере ответ, необходимо закрыть соединение методом **close()**

Еще добавим к request метод decode('utf-8').

```python
def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost'), 5000)
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)
        # отвечаем
        client_socket.sendall('hello world'.encode())
        client_socket.close()
```

Заупстим скрипт, в бразуере перейдем на localhost:5000.

В коноли получили ответ и это хорошо.

```
('127.0.0.1', 50938)
GET /robots.txt HTTP/1.1
Host: localhost:5000
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
Accept: */*
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ru;q=0.8
```

Если же наш порт занят и там включился тайм-аут. Мы можем использовать метод setsockopt, который принимает три аргумента на вход: 1-й SOL_SOCKET - говорит, что мы обращаемся именно к нашему текущему сокету, 2-й SO_REUSEADDR - то, что мы ходим переиспользовать адрес, 3-й единица означает, что мы включае True.

Ставим перед вызовом метода bind.

```python
def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # добавили 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)

        client_socket.sendall('hello world'.encode())
        client_socket.close()
```

Чтобы ответить пользователю определенным образом, создадм переменную response и она будет принимать ответ функции generate_response (сделаем ее еще). Она будет принимать на вход request.

Задача функции generate_response: распарсить requesst и получить HTTP метод и URL запроса.

В функции generate_response определим переменную method и url, которые будут получены с помощью функции parse_request (тоже напишем). 

Функция parse_request забирает из списка метод и урл

```python
def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)

def generate_response(request):
    method, url = parse_request(request)

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall('hello world'.encode())
        client_socket.close()
```

Ответ клиенту будет содежрать заголовок и само тело


Продолжение следует....



































