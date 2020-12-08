---
layout: post
title: 'Переопределение методов в python'
category: python
---

Допустим есть класс

```python
class Lamp:
    def __init__(self):
        self.state = False
        
    def switch_on(self):
        if not self.state:
            self.state = True
            print('Включили')
    
    def switch_off(self):
        if self.state == True:
            self.state = False
            print('Выключили')
        else:
            print('Лампочка уже выключена')
```

Если мы захотим вывести объект, то получим 

```python
print(lamp1)
>>> <__main__.Lamp object at 0x105dfd750>
```

Чтобы при выводе мы получали что-то другое, необходимо переопределить метод ```print``` с помощью ```__repr__```.

Добавим в Класс метод ```__repr__```:

```python
 def __repr__(self):
        return f'лампочка включена - {self.state}'
```

Теперь при вызове ```print()``` получим другой результат

```python
print(lamp1)
>>> лампочка включена - False
```

