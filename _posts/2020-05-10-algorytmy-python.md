---
layout: post
category: python
title: 'Алгоритмы'
---

Тут очень много текста

Нотация Большого О говорит о сложности алгоритма. Например, есть два алгоритма:

- ```O(n)``` - его время возрастает с возрастанием ```n```
- ```O(1)``` - 

В данном случае второй алгоритм эффективнее, потому что его нотация константна и он не зависит от подаваемых данных.

<img src="/assets/img/2020-05-10-algorytmy-python/big-o.png">

Как посчитать сложность алгоритма

<img src="/assets/img/2020-05-10-algorytmy-python/schet.png">

Константы можно откинуть, потому что смотрим только на доминирующую часть при увеличении ```n```. Тут главным квадрат. Даже тройка не существенно, остается только n**2

<img src="/assets/img/2020-05-10-algorytmy-python/schet-2.png">

Цикл например ```for i in range(n)``` это уже как минимум будет ```O(n)```.

Цикл в цикле уже сразу будет ```O(n**2)```.

<img src="/assets/img/2020-05-10-algorytmy-python/prim-1.png">

<img src="/assets/img/2020-05-10-algorytmy-python/prim-2.png">

<img src="/assets/img/2020-05-10-algorytmy-python/schet-3.png">

<img src="/assets/img/2020-05-10-algorytmy-python/prim-4.png">

<img src="/assets/img/2020-05-10-algorytmy-python/prim-5.png">

<img src="/assets/img/2020-05-10-algorytmy-python/prim-6.png">

<img src="/assets/img/2020-05-10-algorytmy-python/prim-7.png">

**Асимптотический анализ** - сравнение затрат времени алгоритмов, выполняющих решение некоторой задачи, при больших объемах входных данных.

**Сложность алгоритма** - это функция, позволяющая определить, как быстро увеличивается время работы алгоритма с увеличением объема данных.

**Основной оценкой роста**, встречающейся в асимптотическом анализе является **О-большое** - верхняя асимптотическая оценка роста временной функции.

# 1. Алгоритмы поиска

Классическая коллекция - список, каждый элемент находится на своей позиции.

## 1.1 Линейный (последовательный) поиск

При линейном поиске движемся слева направо и смотрим на наше искомое значение

```python
def linear_searh(lst, key):
    for idx, item in enumerate(lst): #enumerate дает и значение и ключ
        if key == item:
            return idx
    return -1
```

Эффективность в данном случае можно оценить как количесвто сравнений.

<img src="/assets/img/2020-05-10-algorytmy-python/sravn-1.png">

У нашего последовательного поиска сложность будет O(n) при больших значениях.

## 1.2 Линейный сортированных поиск

Хорошо отрабатывает на небольших значениях. Если мы ищем 7, а список [1, 3, 6, 10, 20, 40], то алгоритм дойдет то 10 и выбросит, что такого элемента нет. Сравнений будет меньше.

```python
def ordered_linear_searh(lst, key):
    for idx, item in enumerate(lst):
        if item == key:
            return idx
        elif item > key:
            return -1
        return -1
```

<img src="/assets/img/2020-05-10-algorytmy-python/sravn-2.png">

## 1.3 Бинарный (двоичный) поиск

Самый крутой поиск. Ищет по половинам сравнивает больше меньше и отсекает ненужное.

<img src="/assets/img/2020-05-10-algorytmy-python/poisk-3.png">

<img src="/assets/img/2020-05-10-algorytmy-python/poisk-2.png">

<img src="/assets/img/2020-05-10-algorytmy-python/poisk-4.png">

**Реализация на python**

```python
def binary_search(lst, key):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if lst(mid) == key:
            return mid
        else:
            if key < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1
```

Большое-О этого алгоритма - **O(log n)**

<img src="/assets/img/2020-05-10-algorytmy-python/binary-summary.png">

## 1.4 Выводы по алгоритмам поиска

- Асимптотическая сложность алгоритма линейного поиска - **O(n)**
- Асимптотическая сложность алгоритма бинарного поиска для упорядоченных списков - **O(nog n)**

# 2. Рекурсия

## 2.1 Бинарный поиск с помощью рекурсии

```python
def binary_search(lst, key):
    if len(lst) == 0:
        return -1
    else:
        mid = len(lst) // 2
        if lst[mid] == key:
            if lst[mid] == key:
                return mid
            else:
                if key < lst[mid]:
                    return binary_search(lst[:mid], key)
                else:
                    return binary_search(lst[mid+1:], key)
```

## 2.2 Алгоритм Евклида (находит наибольший общий делитель)

```python
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)
```

В рекурсии чтобы не зациклиться необходимо найти **базовый случай при котором все останавливается**.

## 2.3 Факториал с рекурсией и без

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

Рекурсия может быть опасна и медленна. Например, факториал лучше находить без рекурсии. Ниже пример кода с замерами по времени у двух функций фаториалов.

```python
def factorial1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


from timeit import Timer

t1 = Timer("factorial1(100)", "from __main__ import factorial1")
print('One', t1.timeit(number=1), 'ms')
t2 = Timer("factorial2(100)", "from __main__ import factorial2")
print('Two', t2.timeit(number=1), 'ms')

>>> One 1.580200000000226e-05 ms
>>> Two 7.277600000000356e-05 ms
```

В пайтоне еще можер упереться в максимальную глубину рекурсии.

## 2.4 Числа Фибоначи с рекурсией и без

**Задача**: вернуть какое-то число Фибоначи **рекурсивно**

```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```

Сложность этого алгоритма: **O(n^2)**

**Задача**: вернуть какое-то число Фибоначи **НЕ рекурсивно**

```python
def fib2(n):
    f = [0, 1, 1]
    for i in range(3, n):
        f.append(f[i-1] + f[i-2])
    return f[len(f)-1]
```

Сложность этого алгоритма: **O(n)** + memory для списка. То же самое можно сделать без списка, чтобы не расходовать память. **Пример ниже**.

```python
def fib3(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
```

# 3. Алгоритмы сортировки

## 3.1 Сортировка пузырьком (Bubble Sort)

<img src="/assets/img/2020-05-10-algorytmy-python/bubble-1.png">

```python
def bubble_sort(lst):
    for counter in range(len(lst)-1, 0, -1):
        for i in range(counter):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

import random
lst = [random.randrange(100) for i in range(9)]
print(lst)
bubble_sort(lst)
print(lst)

>>> [52, 71, 27, 43, 25, 65, 52, 17, 48]
>>> [17, 25, 27, 43, 48, 52, 52, 65, 71]
```

**Сложность алгоритма**: O(n^2) - самый неэффективный метод сортировки

## 3.2 Сортировка вставками (Insertion Sort)

<img src="/assets/img/2020-05-10-algorytmy-python/sort-2.png">

**Сложность алгоритма**: O(n^2) - этот алгоритм хорошо себя зарекомендовал и он используется иногда.

```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > current:
            lst[pos] = lst[pos-1]
            pos = pos - 1
        lst[pos] = current
```

В лучшем случае потребуется только одно сравнение на каждом проходе. Плюс в этом алгоритме мы **сдвигаем**, а не обмениваем (обмениваем в алгоритме сортировки пузырьком). **Операция сдвига быстрее, чем операция обмена** (где-то на треть быстрее). 

## 3.3 Сортировка слиянием (Merge Sorting)

<img src="/assets/img/2020-05-10-algorytmy-python/merge-01.png">

Алгоритм постоянно разбивает список пополам.

```python
def merge_sort(lst):
    
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

import random
lst = [random.randrange(100) for i in range(9)]
print(lst)
merge_sort(lst)
print(lst)

>>> [43, 4, 44, 46, 70, 50, 64, 54, 41]
>>> [4, 41, 43, 44, 46, 50, 54, 64, 70]
```

**Сложность алгоритма:**  O(n log(n))

## 3.4 Quick Sort (изучить самому)

**Доп материалы:**

- Визуализация сортировки есть <a href="https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html">тут</a>















