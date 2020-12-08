---
layout: post
category: python
title: 'Python генераторы'
---

Допустим, у нас есть список со словарями и нужно вытащить оттуда список машин.

```python
jack = {
    'name': 'jack',
    'car': 'bmw e36',
}

john = {
    'name': 'john',
    'car': 'lexus is300 1gen',
}

users = [jack, john]

cars = [person ['car'] for person in users]
print(cars)

>>>['bmw e36', 'lexus is300 1gen']
```


То есть по сути это компактная запись цикла for

Но может быть ситуация, что у пользователя значение ключа car будет пустое, тогда мы получим исключение, поэтому хорошей практикой будет использование метода **get** для словарей (пример ниже), чтобы избежать исключение, также добавим вторым аргументом пустой ключ, если нужного ключа не окажется в словаре.

```python
cars = [person.get('car', '') for person in users]
```

**Фильтрация**

Допустим, есть список с именам и нужно отфильтровать список, оставив только имена, которые начинаются с **j**

```python
names = ['jack', 'alice', 'gena', 'vadim', 'jeka']
new_names = [n for n in names if n.startswith('j')]
print(new_names)

>>>['jack', 'jeka']
```

**другое**

```python
l1 = [x**2 for x in range(10)]
l2 = (x**2 for x in range(10))

print(l1)

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

for i in l2:
    print(i)

>>>0
>>>1
>>>4
>>>9
>>>16
>>>25
```

В генераторе данные создаются по мере нашего обращения к ним.
