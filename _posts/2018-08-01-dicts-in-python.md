---
layout: post
title: 'Dictionaries в python'
category: python
---

Чтобы добавить новую пару ключ-значение, используем квадратные скобки.

```python
>>> eng2sp = dict()
>>> eng2sp['one'] = 'uno'
>>> eng2sp
{'one': 'uno'}
```

Чтобы получить значение по ключу тоже квадратные скобки

```python
>>> eng2sp['two'] = 'dos'
>>> eng2sp['two']
'dos'
```

Есть ли ключ в словаре


```python
>>> 'three' in eng2sp
False
```

Подсчет букв в слове

```python
def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d
```
