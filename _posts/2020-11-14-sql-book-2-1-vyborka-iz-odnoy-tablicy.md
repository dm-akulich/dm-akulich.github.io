---
layout: post
title: Выборка данных из одной таблицы
comments: False
category: sql
tags: sql
---

### Про производительность функции COUNT на больших данных

```sql
-- Вариант 1: COUNT(*)
SELECT COUNT(*)
FROM `test_counts`
-- Вариант 2: COUNT(первичный_ключ)
SELECT COUNT(`id`)
FROM `test_counts`
-- Вариант 3: COUNT(1)
SELECT COUNT(1)
FROM `test_counts`
-- Вариант 4: COUNT(поле_без_индекса)
SELECT COUNT(`fni`)
FROM `test_counts`
-- Вариант 5: COUNT(поле_с_индексом)
SELECT COUNT(`fwi`)
FROM `test_counts`
-- Вариант 6: COUNT(DISTINCT поле_без_индекса)
SELECT COUNT(DISTINCT `fni`)
FROM `test_counts`
-- Вариант 7: COUNT(DISTINCT поле_с_индексом)
SELECT COUNT(DISTINCT `fwi`)
FROM `test_counts`
```

<img src="/assets/img/2020-11-14-sql-book-2-1-vyborka-iz-odnoy-tablicy/1.png">

Для MySQL подтверждается бытующее мнение о том, что ```COUNT(*)``` работает медленнее всего, но неожиданно самым быстрым оказывается вариант с ```COUNT(поле_без_индекса)```. Однако стоит отметить, что на меньшем объёме данных (до миллиона записей) ситуация оказывается совершенно иной — быстрее всего работает ```COUNT(*)```.

MS SQL Server показал ожидаемые результаты: ```COUNT(первичный_ключ)``` оказался самым быстрым, — самым медленным. На меньших объёмах данных этот результат не меняется.

Общая рекомендация состоит в том, чтобы использовать ```COUNT(1)``` как в среднем один из самых быстрых вариантов для разных СУБД и разных объёмов данных.


### Даты и ```WHERE```

Если мы фильтруем по датам, и нужно допустим поулучить от года или месяца, лучше использовать константное сравнение. Ниже пример

```sql
---- OK
...
WHERE  "sb_start" >= TO_DATE('2012-06-01', 'yyyy-mm-dd');

---- Потеря производительности
...
WHERE  YEAR(`sb_start`) = 2012
```

Вместо того, чтобы получить константу (начала диапазона дат) и напрямую сравнивать с ними значения анализируемого столбца таблицы (используя индекс), СУБД вынуждена для каждой записи в таблице выполнять два преобразования, и затем сравнивать результаты с заданными константами (напрямую, без использования индекса, т.к. в таблице нет индексов по результатам извлечения года и месяца из даты).

Запрос, требующий извлечения части поля, приводит к падению производительности от примерно полутора до примерно ста пятидесяти раз.














