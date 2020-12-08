---
layout: post
category: python
title: 'PyEx 05/08. Множества, словари, текст'
---

## Множества 

множества - set

метод add - добавление в множество.

remove(), discard() - удаление из множества. Аргументом передается элемент, который следует удалить. Если элемента в множестве нет, remove вызовет исключение. discard ошибки не вызывает.

Для полной очистки множества можно использовать метод clean()


Множества можно объединять методом .union(). Сами множества А и в при этом не изменяются, а результатом является новое множество, состоящее из элементов множеств А и B.

**А.update(В)** - в результате новое множество не создастся, а расширится множество A

Разность множеств вычисляется методом **difference()** - результатом будет новое множество.

Для того чтобы результат вычисления разности множеств записывался в переменную А, используем команды **A.difference_update(В)**.

Операторы и методы множеств:

- ```<``` - Результатом выражения А<В является True, если все элементы множества А входят в множество в (множество А является подмножеством множества в), причем оба множества не равны. В противном случае значение выражения равно False.
- ```<=``` или ```issubset()``` - результатом выражения А<=В (или выражения ```А.issubset(В)```) является True, если все элементы множества А входят в множество в (множество А является подмножеством множества В), причем допускается равенство множеств. В противном случае значение выражения равно Fаlsе.
- ```>``` - Результатом выражения А>В является True, если все элементы множества В входят в множество А (множество в является подмножеством множества А), причем оба множества не равны. В противном случае значение выражения равно Fа1sе.
- ```>= или issuperset()``` - Результатом выражения А>=В (иди выражения ```А.issuperset(В)```) является True, если все элементы множества в входят в множество А (множество в является подмножеством множества А), причем допускается равенство множеств. В противном случае значение выражения равно Fа1sе.  
- ```isdisjoint()``` - Результатом выражения ```А.isdisjоint(В)``` является значение. True, если пересечение множеств А и в является пустым множеством (то есть если у множеств А и В нет общих элементов). В противном случае значение выражения равно Fа1sе.
- ```in``` - Результатом выражения а in А является значение True, если элемент ```а``` входит в множество ```А```. В противном случае значение выражения равно Fa1sе.

В множестве порядок элементов не фиксирован.


Генератор множества подобен генератору списка, но вся конструкция заключается в фигурные скобки.

Доступ к элементам словаря выполняется по ключу: после имени словаря в квадратных скобках указывается ключ элемента.

Метод keys() позволяет получить доступ к ключам словаря. Для доступа к значениям словаря используют метод values(). Метод items() возвращает кортежи с ключами и значениями элементов словаря. 

Для удаления элемента из словаря применяют метод рор ( ) . Для добавления нескольких элементов используют метод update(). Новый элемент в словар� можно добавить, присвоив значение элементу с новым ключом: после имени словаря в квадратных скобках указывается ключ добавляемого элемента, и, после знака равенства, значение элемента. 

Поверхностная копия словаря создается с помощью метода сору(), а полную копию можно создать с помощью функции deepcopy() из модуля сору. 

Генератор словаря заключается в фигурные скобки, и одновременно нужно создавать два параметра: ключ и соответствующий ему элемент словаря. 
