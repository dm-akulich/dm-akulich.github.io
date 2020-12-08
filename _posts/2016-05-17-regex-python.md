---
layout: post
category: python
title: 'Регулярные выражения в Python'
tags: regex
---

Сайт в помощь <a href="https://regex101.com/#python" rel="nofollow">regex101.com</a>

Документация <a href="https://docs.python.org/3.5/library/re.html">документация по re</a>

Если нам нужно вывести бэкслеш, то используем двойные кавычки

```python
>>> print("hello\"world")
hello"world
```

Raw String

```python
>>> raw_dummy_str = r"This is a \n raw string"
>>> print(raw_dummy_str)
This is a \n raw string
```

Так как некоторые шаблоны regex содержат бэкслеш, то будем использовать 'сырую строку' для записи шаблона.

За regex отвечает модуль ```re```

**Основыне функции re**

- print(re.match) - берет шаблон, берет строку и проверяет подходит ли строка под шаблон.
- print(re.search) - берет строку и находит первую подстроку, которая подходит под данный шаблон.
- print(re.finall) - берет строку и находит все подстроки, которые подходят под данный шаблон.
- print(re.sub) - позволяет заменить все вхождения подстрок, которые подходят под шаблон, чем-нибудь другим.

**Простой пример**

```python
import re
pattern = r"abc"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)
>>> <re.Match object; span=(0, 3), match='abc'>
```

Атрибут span - с какой по какую позицию попало под шаблон.
match - само совпадение


**пример с search**

```python
import re
pattern = r"abc"
string = "babc"
match_object = re.search(pattern, string)
print(match_object)
>>> <re.Match object; span=(1, 4), match='abc'>
```

Работает типа как слайс


## мета-символы

```python
import re
pattern = r"a[abc]c"
string = "aac"
match_object = re.match(pattern, string)
print(match_object)
>>> <re.Match object; span=(0, 3), match='aac'>
```

В квадратных скобках указали символы которые могут быть.


**Пример с findall и search**

Тут будем искать вхождения и заменим их на нужное нам, а именно 'abc'.

```python
import re

pattern = r"a[abc]c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

>>> <re.Match object; span=(0, 3), match='acc'>
>>> ['abc', 'acc', 'aac']
>>> abc, abc, abc
```


##Другие мета-символы 

Допустим, мы хотим найти вхождение вопроса, который бы заканчивался на 'english?' в строке 'Do you speak english?'

```python
import re

pattern = r" english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)

>>> <re.Match object; span=(12, 21), match=' english?'>
```

Так как ? является мета-символом, чтобы найти его в строке необходимо его экранировать с помощью бэкслеша.


Основные мета-символы:

- ```[] - -``` - Можно указать множество подходящих символов, например [a-d], то есть это будут a,b,c,d. [a-Z] - все буквы.
- ```.``` - любой один символ. [a.c], нашел бы все строки "a<любой один символ>c" 
- ```^``` - цикрумфлекс. То, что нам не подходит.

```python
import re
pattern = r"a[^a-zA-Z]c" # нам не подходит любая буква вторым символом
string = "a.c a_c abc"

all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>> ['a.c', 'a_c']
```

Многие дефолтные вещи имею укороченную запись:

- [0-9] ~ \d - цифры
- [^0-9] ~ \D - не цифры
- [ \t\n\r\f\v] - \s - пробельные символы
- [^ \t\n\r\f\v] - \S - не пробельные символы
- [a-zA-Z0-9_] - \w - буквы + цифры + _
- [a-zA-Z0-9_] - \W - не буквы + не цифры + не _


- ```*``` - если используем * после символа ```b```, говорим о том, что нас интересует любое количество символа b, включая ноль.

```python
import re 
pattern = r"ab*a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>> ['aa', 'aba', 'abba']
``` 

- ```+``` - если используем + после символа ```b```, говорим о том, что нас интересует любое количество символа b, больше нуля.

```python
import re 
pattern = r"ab+a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>> ['aba', 'abba']
```

- ```?``` - если используем ? после символа ```b```, говорим о том, что нас интересует любое **ноль или одно** d[вхождение символа b.

- ```{ }``` - в фигурных скобках можем указать конкретное количесвто вхождений, которые нас интересуют. В скобках можно поставить запятую и будет "от-до"

```python
import re 
pattern = r"ab{2}a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>> ['abba']
```

По умолчанию + жадный и ище самое большое вхождение

```python
import re 
pattern = r"a[ab]+a"
string = "abaaba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>> ['abaaba']
```

Чтобы он нашел минимальное вхождение удовлетворяющее условию, можно после ```+``` поставить ```?```

```python
import re 
pattern = r"a[ab]+?a"
string = "abaaba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
>>>['aba', 'aba']
```

## Группировка символов с помощью regex ```( )```

```python
import re 
pattern = r"(test)*"
string = "test"
match = re.match(pattern, string)
print(match)
>>> <re.Match object; span=(0, 4), match='test'>
```

testtest тоже подойдет

```python
import re 
pattern = r"(test)*"
string = "testtest"
match = re.match(pattern, string)
print(match)
>>> <re.Match object; span=(0, 8), match='testtest'>
```

Можно в ```()``` использовать знак логического ИЛИ ```|```



- ```[ ] ``` - 
- ```\``` - 
- ```|``` - 
- ```( )``` - 











