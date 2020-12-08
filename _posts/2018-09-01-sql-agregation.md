---
layout: post
category: sql
title: 'Агрегация, выборки из нескольких источников в SQL'
---


```COUNT(*)``` Возвращает количество строк источника записей.

```COUNT(<имя поля>)``` Возвращает количество значений в указанном столбце.

```SUM(<имя поля>)``` Возвращает сумму значений в указанном столбце.

```AVG(<имя поля>)``` Возвращает среднее значение в указанном столбце.

```MIN(<имя поля>)``` Возвращает минимальное значение в указанном столбце.

```MAX(<имя поля>)``` Возвращает максимальное значение в указанном столбце.

----------
Группировка по категории

```sql
mysql> select * from store limit 5;
+--------------+----------------+--------+----------+
| product_name | category       | price  | sold_num |
+--------------+----------------+--------+----------+
| Trust-Dax    | Snacks         | 252.00 |       20 |
| Statcom      | Air Fresheners | 917.00 |        8 |
| Konksing     | Snacks         | 348.00 |       13 |
| Sancof       | Snacks         | 120.00 |       13 |
| Geo-Ity      | Cakes          | 341.00 |       14 |
+--------------+----------------+--------+----------+
5 rows in set (0.01 sec)

mysql> select category, count(1) from store GROUP BY category;
+-------------------+----------+
| category          | count(1) |
+-------------------+----------+
| Snacks            |       13 |
| Air Fresheners    |       17 |
| Cakes             |       12 |
| Juices            |        6 |
| Tea & Coffee      |       16 |
| Health & Medicine |       11 |
| Bath Products     |        4 |
| Water             |       11 |
| Dental Care       |        3 |
| Candy             |        7 |
+-------------------+----------+
```

**Условие запроса**:
Выведите 5 категорий товаров, продажи которых принесли наибольшую выручку. Под выручкой понимается сумма произведений стоимости товара на количество проданных единиц. Результат должен содержать два столбца: 
название категории,
выручка от продажи товаров в данной категории.

```sql
mysql> select category, SUM(sold_num*price) as result
	-> from store GROUP BY category
	-> ORDER BY result DESC
	-> LIMIT 5;
+----------------+----------+
| category       | result   |
+----------------+----------+
| Air Fresheners | 67816.00 |
| Snacks         | 59991.00 |
| Cakes          | 54172.00 |
| Water          | 53860.00 |
| Tea & Coffee   | 52868.00 |
+----------------+----------+
5 rows in set (0.00 sec)
```

**Условие запроса**
Выведите в качестве результата одного запроса общее количество заказов, сумму стоимостей (бюджетов) всех проектов, средний срок исполнения заказа в днях.


```sql
mysql> SELECT COUNT(project_name) num_of_projects, SUM(budget) as budget, AVG(DATEDIFF(project_finish, project_start)) from project;
+-----------------+-------------+----------------------------------------------+
| num_of_projects | budget      | AVG(DATEDIFF(project_finish, project_start)) |
+-----------------+-------------+----------------------------------------------+
|             100 | 48453245.00 |                                     704.3100 |
+-----------------+-------------+----------------------------------------------+
```

Когда нужно удалить дубликаты в результирующей таблице, то используем DISTINCT.

```sql
select distinct maker from product where type = 'Printer';
```

# SQL-ex задачи

6. Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость


```sql
SELECT DISTINCT product.maker, laptop.speed FROM Product INNER JOIN laptop ON product.model = laptop.model where laptop.hd >= 10 ORDER BY laptop.speed

```

7. Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).

```
SELECT DISTINCT product.model, PC.price FROM Product INNER JOIN PC ON product.model = pc.model WHERE product.maker = 'B'

UNION

SELECT DISTINCT product.model, Laptop.price FROM Product INNER JOIN Laptop ON product.model = laptop.model WHERE product.maker = 'B'

UNION

SELECT DISTINCT product.model, Printer.price FROM Product INNER JOIN Printer ON product.model = printer.model WHERE product.maker = 'B'
```

