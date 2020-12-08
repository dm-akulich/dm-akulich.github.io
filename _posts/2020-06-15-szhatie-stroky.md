---
layout: post
title: 'Задача на сжатие строки'
category: python
tags: python
---

Из **aaaabbbc** нужно получить **a4b3c1**

```python
def rlePress(s):
    l = len(s)  # длина строки
    p = s[0]  # первый символ
    count = 1  # счетчик
    res = ""  # здесь будет результат
    for i in range(l - 1):
        c = s[i + 1]  # следующий символ
        if (c == p):  # если совпадает с предыдущим - увеличим счетчик
            count += 1
        else:  # иначе выведем пару
            res += p + str(count)
            count = 1
        p = c  # текущий стал предыдущим
    res += p + str(count)  # вывод последней пары
    return res


stri = input()
print(rlePress(stri))
```
