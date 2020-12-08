---
layout: post
title: Временные таблицы в SQL
comments: False
category: sql
tags: sql
---


Временные таблицы используются для хранения промежуточных данных при сложных выборках из БД, например при большом количестве ```JOIN``` и ```UNION``` запросов.

**Созданные таблицы доступны до закрытия соединения т.е. до завершения скрипта или отключения MySQL клиента.**

# 1. Создание временной таблицы

```sql
CREATE TEMPORARY TABLE `tmp_table` (
	`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`price` decimal(11,2) unsigned NOT NULL DEFAULT '0.00',
	`sef` varchar(255) NOT NULL,
	`text` text NOT NULL,
	`approve` tinyint(1) NOT NULL DEFAULT '1',
	`date_add` int(11) unsigned NOT NULL DEFAULT '0',
	PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
```

Создание временной таблицы из структуры другой:

```sql
CREATE TEMPORARY TABLE `tmp_table` LIKE `prods`
```

Клонирование таблицы:

```sql
CREATE TEMPORARY TABLE `tmp_table` 
	SELECT * FROM `prods`
```

Создание и наполнение из нескольких таблиц:

```sql
CREATE TEMPORARY TABLE `tmp_table` 
	SELECT 
		`prods`.`name`,
		`urls`.`sef`
	FROM 
		`prods`
	LEFT JOIN 
		`urls`
	ON
		`prods`.`id` = `urls`.`prods_id`
	WHERE
		`prods`.`approve` = 1
```

# 2. Работа с временными таблицами

После создания таблицы, операции с ней, проводятся как с обычными таблицами.

```sql
-- Добавление
INSERT INTO `tmp_table` SET `name` = 'Запись 1', `approve` = 1, `date_add` = UNIX_TIMESTAMP();
 
-- Изменение
UPDATE `tmp_table` SET `approve` = 0 WHERE `id` = 1;
 
-- Удаление
DELETE FROM `tmp_table` WHERE `approve` = 0;
 
-- Выборка
SELECT * FROM `tmp_table` WHERE `approve` = 1;
```
