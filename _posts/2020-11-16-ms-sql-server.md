---
layout: post
title: MS SQL Server
comments: False
category: sql
tags: sql
---

Схема - используется в SQL Server для логического разграниячения таблиц. Нужны чтобы разграничивать права доступа к таблицам. 

<img src="/assets/img/2020-11-16-ms-sql-server/1.png">

На скрине схемы Application, Purscharing. Когда обращаемся к таблице, обращаемся через схему

```sql
SELECT TOP 10 * FROM Sales.OrderLines;

-- ORDER BY
SELECT TOP 10 *
FROM Sales.OrderLines l
ORDER BY l.Description;

-- Разбивка на страницы
--- OFFSET сколько мы пропускаем строк
SELECT * FROM Sales.OrderLines l
ORDER BY l.[Description] OFFSET 20 ROWS FETCH NEXT 50 ROWS ONLY;

-- DISTINCT
-- Уникальные значения
SELECT DISTINCT TOP 15 ContactPersonID
FROM Sales.Orders;
```

К таблице можно обратиться также через сервер

```sql
SELECT * FROM serverName.dataBaseName.schemaName.table.Name;
```

## Приоритет операторов (Transact-SQL)

Оператор с более высоким уровнем выполняется прежде, чем оператор с более низким уровнем.

Level 	| Операторы
------------------
1 |	~ (побитовое НЕ)
2 |	* (умножение), / (деление), % (остаток деления)
3 |	+ (положительное), – (отрицательное), + (сложение), +( объединение), – (вычитание), & (побитовое И), ^ (побитовое исключающее ИЛИ), | (побитовое ИЛИ)
4 |	=, >, <, >=, <=, <>, !=, !>, !< (операторы сравнения)
5 |	NOT
6 |	AND
7 |	ALL, ANY, BETWEEN, IN, LIKE, OR, SOME
8 |	= (присваивание)

## LIKE

LIKE определяет, совпадает ли указанная символьная строка с заданным шаблоном

Символ-шаблон | Описание
-----------------------
% | Любая строка, содержащая ноль или более символов.
_ (подчеркивание)  | Любой  одиночный символ.
[] | Любой одиночный символ, содержащийся в диапазоне (\[a-f\]) или наборе (\[abcdef\]).
\[\^] | Любой одиночный символ, не содержащийся в диапазоне (\[^a-f\]) или наборе (\[^abcdef\]).

```sql
--EQUALS
SELECT * FROM Warehouse.StockItems
WHERE StockItemName = 'Chocolate sharks 250g';

SELECT * FROM Warehouse.StockItems
WHERE StockItemName LIKE 'Chocolate%';

SELECT RecommendedRetailPrice, *
FROM Warehouse.StockItems
WHERE RecommendedRetailPrice BETWEEN 350 AND 500 AND
(StockItemName LIKE 'USB%' OR StockItemName LIKE 'Ride%');

```

# Индексы, профилирование, оптимизация

- Индексы - возволяют выполнять зарпосы быстро
- Протоколирование - позволяет понять, какие нам индексы нужны
- План запросов - по какому алгоритму СУБД будет выполнять запрос
- Какие есть стратегии джоинов и ТП

## Индексирование

### btreee

В классическом случае индекс у нас btreee - типа дерево, где с одной стороны значение больше, с другой - меньше.

<img src="/assets/img/2020-11-16-ms-sql-server/2.png">

В этом случае дерево будет построено так что на первом месте - last_name, потом first_name, потом dob. В самом индексе хранятся ссылки на записи. Вся запись в индеске не хранится. Но если у нас индекс по фамилии, имени и дате рождения, то в индексе целиком имя, фамилия, дата рождения.

***Чем полезен индекс***

**Можно**
- Поиск по полному занчению
- Поиск по левому префиксу
- Поиск по префиксу столбца
- Поиск по диапазону значений
- Поиск по полному совпадению одной части и диапазону другой части
- Запросы только по индексу

**Нельзя**
- Поиск без использования левой части ключа, т.е. если мы хотим получить выборку по дате рождения, то этот индекс никак не поможет.
- Нельзя пропускать столбцы
- Оптимизация после поиска в диапазоне

### hash-индексы

<img src="/assets/img/2020-11-16-ms-sql-server/3.png">

Явно они практически никтогда не создаются.

Суть его в том, что есть ключ, по ключу считается хэш, далее к хэшу прикрепляетяс информация о том на каких записях значение с этим хешом встречается. 


<img src="/assets/img/2020-11-16-ms-sql-server/4.png">

### Кластреные и некластерные индексы в MS SQL

[Документация](https://docs.microsoft.com/ru-ru/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15)

Индекс является структурой на диске, которая связана с таблицей или представлением и ускоряет получение строк из таблицы или представления. Индекс содержит ключи, построенные из одного или нескольких столбцов в таблице или представлении. Эти ключи хранятся в виде структуры сбалансированного дерева, которая поддерживает быстрый поиск строк по их ключевым значениям в SQL Server.

Таблица или представление может иметь индексы следующих типов.

- Кластеризованный
    - Кластеризованные индексы сортируют и хранят строки данных в таблицах или представлениях на основе их ключевых значений. Этими значениями являются столбцы, включенные в определение индекса. Существует только один кластеризованный индекс для каждой таблицы, так как строки данных могут храниться в единственном порядке.  
    - Строки данных в таблице хранятся в порядке сортировки только в том случае, если таблица содержит кластеризованный индекс. Если у таблицы есть кластеризованный индекс, то таблица называется кластеризованной. Если у таблицы нет кластеризованного индекса, то строки данных хранятся в неупорядоченной структуре, которая называется кучей.

- Некластеризованный
    - Некластеризованные индексы имеют структуру, отдельную от строк данных. В некластеризованном индексе содержатся значения ключа некластеризованного индекса, и каждая запись значения ключа содержит указатель на строку данных, содержащую значение ключа.
    - Указатель из строки индекса в некластеризованном индексе, который указывает на строку данных, называется указателем строки. Структура указателя строки зависит от того, хранятся ли страницы данных в куче или в кластеризованной таблице. Для кучи указатель строки является указателем на строку. Для кластеризованной таблицы указатель строки данных является ключом кластеризованного индекса.
    - Вы можете добавить неключевые столбцы на конечный уровень некластеризованного индекса, чтобы обойти существующее ограничение на ключи индексов и выполнять полностью индексированные запросы. Дополнительные сведения см. в статье Create Indexes with Included Columns. Дополнительные сведения об ограничениях на ключи индексов см. в разделе Спецификации максимально допустимых параметров SQL Server.

Как кластеризованные, так и некластеризованные индексы могут быть уникальными. Это означает, что никакие две строки не имеют одинаковое значение для ключа индекса. В противном случае индекс не является уникальным, и несколько строк могут содержать одно и то же значение.

Обслуживание индексов таблиц и представлений происходит автоматически при любом изменении данных в таблице.

### Индексы и ограничения

Индексы создаются автоматически при определении ограничений PRIMARY KEY или UNIQUE на основе столбцов таблицы. Например, при создании таблицы с ограничением UNIQUE Компонент Database Engine автоматически создает некластеризованный индекс. При настройке PRIMARY KEY Компонент Database Engine автоматически создает кластеризованный индекс, если он еще не существует. Если вы пытаетесь применить ограничение PRIMARY KEY в существующей таблице, для которой уже создан кластеризованный индекс, SQL Server применяет первичный ключ с помощью некластеризованного индекса.

- [Руководство по проектированию индексов SQL Server](https://docs.microsoft.com/ru-ru/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver15)
- [Создание кластеризованных индексов](https://docs.microsoft.com/ru-ru/sql/relational-databases/indexes/create-clustered-indexes?view=sql-server-ver15)
- [Создание некластеризованных индексов](https://docs.microsoft.com/ru-ru/sql/relational-databases/indexes/create-nonclustered-indexes?view=sql-server-ver15)

### Трехзначная логика, NULL

Понятно, что мы используем ```IS NULL```, но можно включить опцию ```SET ANSI_NULLS OFF```

```sql
SET ANSI_NULLS OFF
SELECT OrderID, PickingCompletedWhen
FROM Sales.Orders
WHERE PickingCompletedWhen = NULL;
GO
```

Теперь покажутся только ```NULL```

Конкатенация с NULL дает NULL. Но это поведение можно отключить, через ```SET CONCAT_NULL_YIELDS_NULL```

```sql
SELECT 'abc' + NULL -- ничего не выведет

SET CONCAT_NULL_YIELDS_NULL OFF
SELECT 'abc' + NULL
SET CONCAT_NULL_YIELDS_NULL ON
```

<img src="/assets/img/2020-11-16-ms-sql-server/5.png">


Арифметические операции с ```NULL``` дает ```NULL```.

### Особенности работы с датами

Мы можем явно указать тип даты

```sql
SET DATEFORMAT mdy
SELECT * FROM Sales.Orders
WHERE OrderDate > '01.05.2016' -- пятое января
ORDER BY OrderDate
GO
```

Извлечение дат

```sql
-- DATEPART
SELECT o.OrderID,
    o.OrderDate,
    DATEPART(m, o.OrderDate) AS OrderMonth,
    DATEPART(d, o.OrderDate) AS OrderDay,
    DATEPART(yy, o.OrderDate) AS OrderYear
FROM Sales.Orders AS o;
```


### План запроса

В Azure Studio открывается через ```cmd+M```.


# INSERT, подзапросы, CTE, временные таблицы.

## INSERT

```sql
INSERT INTO Warehouse.Colors
    (ColorID, ColorName, LastEditedBy)
VALUES
    (NEXT VALUE FOR Sequences.ColorID, 'Ohra', 1),
    (NEXT VALUE FOR Sequences.ColorID, 'Ohra2', 2),
    (NEXT VALUE FOR Sequences.ColorID, 'Ohra3', 1),
```

Sequences - отдельная сущность вне таблицы

Можно через переменные вставлять.

```sql
DECLARE
    @colorId INT,
    @LastEditedBySystemUser INT,
    @SystemUserName NVARCHAR(50) = 'Data Conversion Only'

SET @colorId = NEXT VALUE FOR Sequences.ColorID;

SELECT @LastEditedBySystemUser = 2
FROM [Application].People
WHERE FullName = @SystemUserName

INSERT INTO Warehouse.Colors
    (ColorID, ColorName, LastEditedBy)
VALUES
    (@colorId, 'Ohra2', @LastEditedBySystemUser);
```

### WITH (CTE)

Можем использовать WITH для временной выборки таблицы

```sql
WITH Customers AS
(
    SELECT TOP 1
        s.CustomerID,
        s.CustomerName
        FROM Sales.Customers as s
) UPDATE Customers
SET CustomerName = 'no';
```

Это типа вьюха на один запрос.

# Windows Functions

Что такое окно? 

```sql
Function() OVER(окно, по которому идет подсчет) /* Агрегирующая функция может быть любой */

FUNC() OVER(
    PARTITION BY [список полей]
    ORDER BY
    ROWS/RANGE
)

RANK() OVER (ORDER BY username)
RANK() OVER (PARTITION BY city ORDER BY username)
```

<img src="/assets/img/2020-11-16-ms-sql-server/6.png">

```PARTITION BY``` похоже на ```GROUP BY```

Какие функции бывают? 

<img src="/assets/img/2020-11-16-ms-sql-server/7.png">

```sql
--заказы и оплаты по заказам
SELECT Invoices.InvoiceId, Invoices.InvoiceDate, Invoices.CustomerID, trans.TransactionAmount
FROM Sales.Invoices as Invoices
	join Sales.CustomerTransactions as trans
		ON Invoices.InvoiceID = trans.InvoiceID
WHERE Invoices.InvoiceDate < '2014-01-01'
ORDER BY Invoices.InvoiceId, Invoices.InvoiceDate
```

<img src="/assets/img/2020-11-16-ms-sql-server/8.png">

Вывод статистики по запросам

```sql
SET STATISTICS TIME ON; --Для вывода статистики
SET STATISTICS IO ON; --Для вывода статистики

SELECT P.PersonID, P.FullName, COUNT(*)
FROM Sales.Invoices AS I
	JOIN Application.People AS P
	ON P.PersonID=I.SalespersonPersonID
GROUP BY P.PersonID, P.FullName;
```

```
CPU time = 0 ms,  elapsed time = 0 ms.
```

С помощью этой команды можно сравнивать качество между двух запросов.

Проценты в плане это что-то дорогое. ЛУчше смотреть на статистики.


























