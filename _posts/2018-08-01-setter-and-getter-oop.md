---
layout: post
category: python
title: 'Setter и Getter в Python ООП и @classmethod'
---

```python
class Point:
    __count = 0
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    @classmethod
    def count_points(cls):
        return cls.__count

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return f"Я - точка: координата x = {self.__x}, координата y = {self.__y}"

    # Properties for X (вариант реализации 1)
    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    x = property(get_x, set_x)

    # Properties for Y (вариант реализации 2)
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

point = Point(10, 20)
print(point)

point.move_to(100, 200)
print(point.x, ' : ', point.y)

point.move_by(10, 20)
print(point.x, ' : ', point.y)

point.x = 30
point.y = 40
print(point)
point2 = Point(10, 20)
print(Point.count_points())
```

**Вывод**

```bash
>>> Я - точка: координата x = 10, координата y = 20
>>> 100  :  200
>>> 110  :  220
>>> Я - точка: координата x = 30, координата y = 40
>>> 2
```

