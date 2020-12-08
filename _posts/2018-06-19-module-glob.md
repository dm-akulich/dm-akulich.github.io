---
layout: post
category: python
title: 'Python модуль glob'
---

glob - модуль для поиска файлов по паттерну

```python
import glob
p = '/Users/dimaakulich/dev/examples/OOP/'
finded = glob.glob1(p, '*.txt')
print(finded)

>>> ['hello.txt']
```
