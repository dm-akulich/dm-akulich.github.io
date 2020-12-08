---
layout: post
title: 'Asyncio'
category: python
---

Главный элемент любой асинхронной программы - **событийный цикл (event_loop)**. Event Loop является менеджером или планировщиком задач. И суть его работы заключается в некотором реагировании на какие-то события.

Примерно типа "когда наступает событие **А**, отреагирует на него событием **B**".

В модуле asyncio в событийном цикле крутятся эклмепляры класса Task, которые по сути являются контейнерами для корутин.

Эклемпляры класса Task это и есть те действия, которые должны выполняться асинхронно.


# Небольшой пример (Это синтаксис python 3.4)

## Шаг 1

```python
import asyncio
from time import time


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)  # делаем задержку с помощью asyncio.
        # Используем yield from, Потому что фунция является генератором.


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} sencomds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    pass


if __name__ == '__main__':
    main()
```

**@asyncio.coroutine** - декоратор превращает функцию в генератор. В этом можно убедиться, воспользовавшись методом модуля inspect - *inspect.isgenerator()*.

В функции **main()** описан событийный цикл.

Функции ```print_nums``` и ```print_time``` - функции, которые могут выполняться самостоятельно, они могут быть независимыми сами по себе.

## Шаг 2

Наши корутины необъодимо обернуть в экземпляры **Класса Task()** и поставить в очередь событийного цикла. Это делается с помощью метода ```ensure_future```.

После того как мы создали переменыые ```task1``` и ```task2```, нам нужно как-то получить их результат.
Для этого есть специальнй метод, который называется ```asyncio.gather()```, 


```python
import asyncio
from time import time


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)  # делаем задержку с помощью asyncio.
        # Используем yield from, Потому что фунция является генератором.


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # открываем событийный цикл
    loop.run_until_complete(main())  # выполняем событийный цикл
    loop.close()  # закрываем событийный цикл

```


# Пример 2 (Это синтаксис python 3.5+)

С обновой пришли изменения и теперь вместо декоратора используется синтаксис ```async def foo()```.

А вместо ```yield from ...``` теперь ```await ...```. То есть вызов асинхронной функции (корутины) теперь осуществляется с помощью ключевого слова ```await```.

```python
import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)  # делаем задержку с помощью asyncio.
        # Используем yield from, Потому что фунция является генератором.


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # открываем событийный цикл
    loop.run_until_complete(main())  # выполняем событийный цикл
    loop.close()  # закрываем событийный цикл
```



# Пример 3 (Это синтаксис python 3.7+)

Вместо ```ensure_future``` теперь ```create_task```.

И теперь чтобы запустить асинхронную программу **НЕ нужно использовать:**

```python
if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # открываем событийный цикл
    loop.run_until_complete(main())  # выполняем событийный цикл
    loop.close()  # закрываем событийный цикл
```

Теперь используем:


```python
if __name__ == '__main__':
    asyncio.run(main())
```

В итоге программа выглядит так:

```python
import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)  # делаем задержку с помощью asyncio.
        # Используем yield from, Потому что фунция является генератором.


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()  # открываем событийный цикл
    # loop.run_until_complete(main())  # выполняем событийный цикл
    # loop.close()  # закрываем событийный цикл
    asyncio.run(main())

```


# Более практичный пример

Суть программы: скачиваем картинки и замеряем время на эффективность.

## Пример **без** использования asyncio

```python
import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


if __name__ == '__main__':
    main()

>>> 10.919480800628662
```

Время выполнения 10 секунд.

## Пример **c** использованием asyncio

Так как у asyncio нет api для работы с http, импортируем aiohttp.

```python
import requests
import asyncio
import aiohttp
from time import time


def write_image(data):
    filename = 'file-{}'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = 'https://loremflickr.com/320/240'

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)


>>> 2.522386074066162
```

Время выполнения 2 секунды.
