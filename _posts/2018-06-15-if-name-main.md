---
layout: post
category: python
title: 'if __name__== main в Python'
---

Что значит ```if __name __ == '__main__'``` в python

Интерпритатор читает код сверху вниз. Но перед тем как прочитать его, он определяет несколько специальных встроенных переменных.

Вызвать все эти переменные можно с помощью функции globals

```Python
print(globals())

>>> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external..........
```

Как видно в самом начаеле переменной __name__ было присвоено значение __main__. Переменная name хранит имя модуля.

Убедимся в этом.

```
print('imported from:', __name__)
>>>imported from: __main__
```

Допустим у нас в директории есть два модуля hello.py и mainfile.py

```python
# work_directory/hello.py
```

```python
# work_directory/mainfile.py
from hello import *
>>>imported from hello: hello
```

Как видно, значение переменной изменилось. И hello в данном случае это имя модуля и которого был произведен импорт. То есть переменная name хранит имя модуля. Значение main переменная принимает когда скрипт мы запускаем скаомстоятельно, и имя текущего модуля.

## Как это используем

То есть условный оператор ```if __name__ == '__main__':``` определяет значение переменной ```__name__```. И если значение main (то есть модуль был запущен как самостоятельынй),  то выполняется кусок кода, который был задписан в теле этого условного оператора.


Использовать эту констукцию можно, когда мы планируем использовать наш моудль как самостоятельный и как дополнительный. Чтобы ничего не вылезало. Например левые выводы.

**Пример**

```python
# work_directory/hello.py
print('Какой-то левый вывод')
```

```python
# work_directory/mainfile.py
from hello import *
print('imported from:', __name__)
>>>Какой-то левый вывод
>>>imported from hello: hello
```

Как видим, какой-то левый вывод


**Как должно быть**

```python
# work_directory/hello.py
if __name__=='__main__':
    print('Какой-то левый вывод')
```

```python
# work_directory/mainfile.py
from hello import *
print('imported from:', __name__)
>>>imported from hello: hello
```
