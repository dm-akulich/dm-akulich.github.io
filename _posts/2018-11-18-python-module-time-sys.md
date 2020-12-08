---
layout: post
title: 'Модули sys и time. Работа с файловой системой'
category: python
---


```python
import time

print (time.asctime())

import sys

print(sys.stdin.readline())

def my_age():
	print('how old are you?')
	age = int(sys.stdin.readline())
	if age < 18:
		print('young')
	else:
		print('old')

my_age()

```


##Файлы и работа с файловой системой

```python
f = open("test.txt", 'r')
print(f)
>>> <open file 'test.txt', mode 'r' at 0x10d128810>
```

второй аргумент функции open - ключ. "r" - открываем на чтение

- ```r``` - read. Открыть в режиме для чтения (по умолчанию)
- ```w``` - write. Открыть для записи, содержимое файла стирается
- ```a``` - append. Открыть для записи. Запись ведется в конец
- ```b``` - binary. Открыть в бинарном режиме
- ```t``` - text. Открыть в текстовом режиме (по умолчанию)
- ```r+``` - открыть для чтения и записи
- ```w+``` - открыть для чтения и записи. Содержимое файла стирается

Можно сочетать режимы, например ```rb``` - открыть в бинарном формате для чтения.

FileObject после работы с ним нужно обязательно закрывать. Чтобы освобождать системные ресурсы. (Метод .close())



```python
f = open("test.txt", 'r')
x = f.read(5)
print(x)

f.close()
>>> hello
```

Вывели первые 5 символов файла.

Чтобы разбить любой файл по строкам, используем метод ```splitlines()``` - метод строки

```python
f = open("test.txt", 'r')
x = f.read()
x = x.splitlines()

print(x)
f.close()
>>> ['hello world', 'Minsk 1400', 'Moscow 6500', 'Kyiv 12300']
```

##Считываем по строкам

```python
f = open("test.txt", 'r')
x = f.readline()
x = x.rstrip()
print(x)
x = f.readline()
x = x.rstrip()
print(x)

f.close()

>>> hello world
>>> Minsk 1400
```

Можно также испольщовать метод rstrip, который удаляет служебные символы по бокам. Метод readline - считываем по строкам.


## Запись в файл


```python
f = open("test.txt", 'w')
f.write('hello')
f.close()
```

Если мы знаем, что мы будем добавлять разные строки, то лучше использовать метод join(). Join принимает один аргумент - список строк.

```python
f = open("test.txt", 'w')
lines = ['hello', 'world']
contents = "\n".join(lines)
f.write(contents)
f.close()
```

##Что делать, если с момент как мы открыли файл до момента когда мы его закрыли, произошла ошибка

Чтобы себя обезопасить себя от такой ситуации, можно использовать метод ```with```.

В конструкции with мы можем открыть сразу несклько файлов, просто указав их через заптую.

```python
with open("test.txt") as f, open("test_copy.txt", 'w') as w:
    for line in f:
        w.write(line)
```


## Библиотеки os и os.path

Функция ```os.listdir()``` - можно перечислить все файлы и папки в директории. Аргументом идет относительный путь

```python
import os
import os.path

print(os.listdir())
>>>'nano.save', 'reply_3380_5.txt', 'dataset_3363_2_1.txt', 's.py', '1.12_14.py', '1.3.5.3.py', '1.12_20.py', '1.3.4.2.py', '1.3.7.5.py', '2.2.3.py', '1.12_5.py', 'dataset_3363_2_2.txt', '1.12_10.py'
```

Функция ```os.getcwd()``` - показать где текущая папка

```python
import os
import os.path

print(os.getcwd())
>>>/Users/dimaakulich/Documents/dev/stepik
```

Функция ```os.path.exists("/filename.txt")``` - существует ли файл или директория.

Функция ```os.path.isdir()```, ```os.path.isfile()``` - является ли путь папкой или файлом.

Функция ```os.path.abspath('filename.txt')``` - чтобы узнать абсолютный путь файла или папки.

Функция ```os.chdir("directoryname")``` - чтобы сменить текущую папку.

```python
print(os.getcwd())
os.chdir("alice")
print(os.getcwd())

>>>/Users/dimaakulich/Documents/dev/stepik
>>>/Users/dimaakulich/Documents/dev/stepik/alice
```

Функция ```os.walk(".")``` - позволяет рекурсивно пройтись по папкам, подпапкам и тд. Функция повзращает кортеж из трех элементов:

- Первое значение - строковое представление директории, которую рассматривает генератор.
- Второе - список из всех подпапок, которые есть в диретории
- Третий - список всех файлов, которые есть в диретории.

```python
import os
import os.path

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
```

##Как копировать файлы

Нужно импортировать библиотеку shutil. Функция shutil.copy("tests/test1.py", "tests/test2.py") - аргументы тут откуда и куда копировать.

```python
import shutil

shutil.copy("tests/test1.py", "tests/test2.py")
```

Скопировать целиком папку можно с помощью функции ```shutil.copytree("tests1", "tests2")```











