---
layout: post
category: python
title: 'Автоматическая мемоизация'
---

В Python есть встроенный декоратор для автоматической мемоизации любой функции.

Декоратор ```@functools. lru_cache()```.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(5))
    print(fib(50))

--> 5
--> 12586269025
```

