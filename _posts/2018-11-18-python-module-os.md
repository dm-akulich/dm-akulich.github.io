---
layout: post
title: 'Модуль OS Python'
category: python
---


OS позволяет рабоать с системой и файлами ОС

```python
import os
print ('Наша os - ', os.name)
```

## Узнаем пути для системных папок
Переменные окружения - специальные переменыые в которых хранятся пути до каких-то системных папок

```python
print('Список переменных окружения: \n')
print(os.environ)
```




## Получаем список файлов и папок в указанной папке

```python
print(os.listdir('E:/'))
```


## Создаем папку

```python
os.makedirs('E:/test/', exist_ok=True)
```

## Удаляем файл

```python
if (os.path.exists('E:/1.txt')):
	os.remove('E:/1.txt')
```

## Перемещаем и переименовывем файл

```python
if (os.path.exists('E:/2.txt')): # Если такой файл существует 
	os.replace('E:/2.txt', 'E:/test/3.txt')
```

## Открывает файл в системе с программой по умолчанию

```python
if (os.path.exists('E:/test/3.txt')):
	os.starfile('E:/test/3.txt')
```
