---
layout: post
title: 'Асинхронность в Python #7 Asyncio, async/await'
category: python
---

Модуль asyncio - модуль, который предназначен для создания событийных циклов.

В модуле async используется класс Task. Он является подклассом класса Future. Который является типа заглушкой. 

Корутины - сама логика нашей программы.

# Пример 1. 

Будет две функции. Одна будет выводить на печать числа от нуля до бесконечности, а другая - будет выводить на печать сообщение (время) с временными промежутками. 

Шаблон будет такой.

```python
def print_nums():
    pass

def print_time():


def main():
    pass

if __name__ == "__main__":
    pass
```

**Продолжение**

В первой функции мы используем функцию ```asyncio.sleep(1)``` - это задержка в 1 сек, чтобы числа не летели быстро, из модуля asyncio.

Так как функция асинхронная, то есть это генератор в данный момент, мы должны использовать ```yield from```.

Вторая функция считает время, там тоже используем ```asyncio.sleep(1)```.

```python
import asyncio
from time import time

@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1 
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 5 == 0:
            print("{} seconds have passed.".format(count))
        count += 1
        yield from asyncio.sleep()


@asyncio.coroutine
def main():
    pass

if __name__ == "__main__":
    pass
```

Основной функционал готов. Чтобы они работали асинхронно, нужно передать их в событийный цикл, который будет определять, в какой момент контроль выполнения потоком будет передаваться в одну из них. Это будет сделано в функции main, которая тоже будет корутиной.

Корутины нужно обернуть в экземпляры класса Task и поставить в очередь событийного цикла. Это делаеться с помощью метода ```ensure_future()```. Эта функция обеспечивает созданеи объекта будущего. В функцию передаем функцию-корутину ```task1 = asyncio.ensure_future(print_nums())```. Вторую функцию также оборачиваем. С помощью метода ```ensure_future``` они попали в очередь событийного цикла.

Теперь нужно дождаться их результата. Чтобы это сделать, нужно использовать специальный метод ```gather```, он тоже генератор. Обернули ```yield from asyncio.gather(task1, task2)```.

Потом запускаем это с помощью ```get_event_loop```. В конце не забываем закрыть ```close``` 

```python
import asyncio
from time import time

@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1 
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 5 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
``` 
 
Запустив в интерактивном режиме все работает.

# Пример 1 (Дополнение. Синтаксис начиная с python 3.7) 

Теперь с python 3.7 были некоторые изменения и тот код, что выше, можно заменить на тот, что ниже и ничего не поменяется.

```python
import asyncio
from time import time

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1 
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 5 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
```

# Пример 2. 

Задача: есть сайт с картинками-загулшками. Будем скачивать оттуда картинки https://loremflickr.com/

Будем скачивать в синхронном и асинхронном стиле и посмотерим время и того и того.

## В синхронном стиле

```python
import requests
from time import time

url = 'https://loremflickr.com/320/240'

def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:# wb - writebinary
        file.write(response.content)

def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))
    print(time() - t0)

if __name__ == "__main__":
    main()

>>> 11 sec
```

## Асинхронный стиль

```python
import asyncio
import aiohttp

def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read() # возвращает бинарные данные
        write_image(data)


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)
```










