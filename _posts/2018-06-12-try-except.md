---
layout: post
category: python
title: 'try и except'
---

Импользеум, чтобы ловить ошибки, которые могут возникнуть

Общий синтуксис такой:

```python
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
```

Задача нужно рассчитать соль в продукте

```python
def calc(m):
    m = int(m)
    return 10 * m / 1000

print(calc('1000'))
```

Все ок и это работает, но могут быть введены не числа, и тогда выскочит ошибка.

Сделаем так, что если возникает исключение, управление переходит в блок except и введенное значение будет равно нулю.

```python
def calc(m):
    try:
        m = int(m)
    except Exception:
        m = 0
    return 10 * m / 1000

print(calc('ads'))

>>>0.0
```

Блок **else** выполняется в том случае, если исключение не произошло.

```python
def calc(m):
    try:
        m = int(m)
    except Exception:
        m = 0
        return 'something wrong'
    else:
        return 10 * m / 1000

    finally:
      print('Function end.')

print(calc('ads'))

>>>something wrong
```

Блок **finally** отвечает за тот кусок кода, который выполняется в любом случае.

Выведем что это за ошибка.

```python
def calc(m):
    try:
        m = int(m)
    except Exception as e:
        print(e)
        m = 0
        return m
    else:
        return 10 * m / 1000

print(calc('ads'))

>>>invalid literal for int() with base 10: 'ads'
>>>0
```

Для каждого типа ошибок можно определять различные поведения. Если ValueError то..., если ZeroDivision то....

```python
def calc(m):
    try:
        m = int(m)
    except ValueError:
        print(e)
        m = 0
        return m
    except TypeError:
        pass
    except FileNotFoundError:
        pass
    else:
        return 10 * m / 1000

print(calc('ads'))
```
