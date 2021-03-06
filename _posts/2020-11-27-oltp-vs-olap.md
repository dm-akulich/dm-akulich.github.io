---
layout: post
title: OLTP и OLAP в SQL
comments: False
category: sql
tags: sql
---

*Источник: Джуба С., Волков А. - Изучаем PostgreSQL 10*

<a href="https://coderlessons.com/tutorials/bolshie-dannye-i-analitika/teoriia-khraneniia-dannykh/12-skhema-zvezd-i-snezhinok" rel="nofollow" target="_blank">Схема звезд и снежинок</a>

Обычно база данных настраива- ется для работы в одном из двух режимов:
- оперативной транзакционной обработки (online transaction processing – **OLTP**)
- оперативного анализа данных (online analytical processing – **OLAP**)

Если база данных работает в качестве серверной части приложения, то требуется **OLTP-решение**. Приложение, работающее с такой базой данных, выполняет транзакцию всякий раз, как пользователь что-то делает: создает учетную запись, изменяет пароль, вводит в систему новый автомобиль, создает или изменяет объявление и т. д. Любое действие такого рода подразумевает транзакцию в базе, в результате которой создается, обновляется или удаляется одна или несколько строк в одной или нескольких таблицах. Чем больше пользователей работает с системой, тем чаще выполняются транзакции.

Ключевые характеристики базы данных, **работающей в режиме OLTP**:
- нормализованная структура;
- относительно небольшой объем данных;
- относительно большое количество транзакций;
- каждая транзакция невелика, затрагивает одну или несколько записей;  пользователи обычно выполняют всевозможные операции с данными: выборку, вставку, удаление и обновление.

Если база данных играет роль источника данных для отчетов и для анализа, то требуется **OLAP-решение**. Это прямая противоположность OLTP: данных много, но изменяются они редко. Количество запросов сравнительно мало, но сами запросы большие и сложные, они требуют чтения и агрегирования огромного количества данных. Производительность измеряется временем выполнения запросов. OLAP-решения часто называют **хранилищами**, или **складами данных**.

**База данных, работающая в режиме OLAP**, обладает следующими характеристиками:
- денормализованная структура;
- относительно большой объем данных;
- относительно небольшое количество транзакций;
- каждая транзакция велика, затрагивает миллионы записей;
- пользователи обычно выполняют только выборку.

## Извлечение, преобразование и загрузка

Рассмотрим задачу о загрузке журналов HTTP-доступа в базу данных и под- готовки их для анализа. Подобные задачи называются **извлечением**, **преобразованием** и **загрузкой** (extract, transform, load – **ETL**).

Можем загрузить файлы из CSV в таблицу например так:

```sql
CREATE TABLE dwh.access_log
(
  ts timestamp with time zone, 
  remote_address text,
  remote_user text,
  url text,
  status_code int,
  body_size int,
  http_referer text,
  http_user_agent text
);

\copy dwh.access_log FROM 'access.log' WITH csv delimiter ';'
```

## Моделирование данных для OLAP

Большая таблица в хранилище данных, содержащая субъект анализа, обычно называется **таблицей фактов**. Журнал доступа по HTTP, который мы обсуждали в предыдущем разделе, как раз и играет роль таблицы фактов.

Не имеет смысла выполнять какие-либо аналитические запросы к таблице фактов, включающие группировку по ```car_id```, не понимая, что стоит за значениями поля ```car_id```. Следовательно, таблица ```car``` тоже должна присутствовать в хранилище. Разница между этой таблицей и таблицей фактов состоит в том, что в таблицу фактов данные постоянно загружаются, а таблица ```car``` в основном статична. Количество записей в таблице ```car``` во много раз меньше. Такие таблицы, служащие для преобразования идентификаторов в имена, называются справочными таблицами, или таблицами измерений. В таблице ```car``` имеется внешний ключ ```car_model_id```, указывающий на запись в таблице ```car_model```, именно он и используется для преобразования идентификатора в модель и марку автомобиля.

Обычно таблица фактов используется так: большие запросы **SELECT** выполняются не слишком часто, но читают огромное количество записей, исчисляемое миллионами или десятками миллионов. В таком случае любые дополнительные операции сервера обходятся очень дорого. Это касается и соединения таблицы фактов с таблицами измерений.

Поэтому данные нередко подвергают денормализации. На практике это означает, что соединение таблиц производится заранее и результат сохраняется в новой таблице. Например, если бы записи журнала доступа были отображены на ```car_id```, как в предыдущем разделе, а аналитическая задача состояла бы в вычислении статистических показателей о марках машин, то нам пришлось бы выполнить два соединения: ```access_log``` с ```car``` и ```car``` с ```car_model```. Это дорого.
Для экономии времени имеет смысл соединить таблицы ```car``` и ```car_model``` и сохранить результат в отдельной таблице. Она уже не будет иметь нормальную форму, потому что одна и та же модель встречается в ней много раз. Конечно, это означает дополнительный расход места на диске. Но это разумный компромисс, потому что опрос таблицы фактов станет быстрее, если производить соединение с одной этой таблицей, а не с двумя таблицами, ```car``` и ```car_model```.
Можно было бы вместо этого завести поле ```car_model_id``` прямо в таблице фактов и заполнять его в процессе **ETL**. Такая структура тоже денормализована, она тоже потребляет больше места, но запрос становится проще.
Таблица фактов может ссылаться на таблицы измерений. А таблица измерений может, в свою очередь, ссылаться на другие таблицы измерений. Такая организация в терминологии OLAP называется схемой типа **«снежинка»** и может выглядеть следующим образом:

<img src='/assets/img/2020-11-27-oltp-vs-olap/1.png'>

Если структура денормализована и таблицы измерений не соединяются между собой, то получается схема типа **«звезда»**, вот такая:

<img src='/assets/img/2020-11-27-oltp-vs-olap/2.png'>

Плюсы и минусы есть у обоих подходов, и, разумеется, ничто не мешает использовать гибридные схемы, в которых **«звезда»** сочетается со **«снежинкой»**. Обычно это вопрос компромисса между сложностью, производительностью и удобством сопровождения.











































































