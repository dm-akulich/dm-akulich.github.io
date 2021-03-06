---
layout: post
title: Как настроить фильтры для Яндекса в GA для SEO?
comments: true
category: Web-analytics
tags: google-analytics
---

Необходимо создать 4 фильтра:

### Замена «yandex.by/referral» на «yandex/organic»-1

- Название фильтра ```Замена «yandex.by/referral» на «yandex/organic»-1```
- Тип фильтра: ```Пользовательский``` -> ```Расширенный```
- *Поле A -> Извлечь A*: Источник кампании ```^yandex\.by$```
- *Поле В -> Извлечь В*: Канал кампании ```referral```
- *Вывод в -> Конструктор*: Канал кампании ```organic```
- ✔️ Поле А обязательно для заполнения
- ✔️ Поле Б обязательно для заполнения
- ✔️ Перезаписать поле вывода
- ▢ С учетом регистра


### Замена «yandex.by/referral» на «yandex/organic»-2

- Название фильтра ```Замена «yandex.by/referral» на «yandex/organic»-2```
- Тип фильтра: ```Пользовательский``` -> ```Расширенный```
- *Поле A -> Извлечь A*: Источник кампании ```^yandex\.by$```
- *Поле В -> Извлечь В*: Канал кампании ```organic```
- *Вывод в -> Конструктор*: Канал кампании ```yandex```
- ✔️ Поле А обязательно для заполнения
- ✔️ Поле Б обязательно для заполнения
- ✔️ Перезаписать поле вывода
- ▢ С учетом регистра

### Замена «yandex.ru/referral» на «yandex/organic»-1

- Название фильтра ```Замена «yandex.ru/referral» на «yandex/organic»-1```
- Тип фильтра: ```Пользовательский``` -> ```Расширенный```
- *Поле A -> Извлечь A*: Источник кампании ```^yandex\.ru$```
- *Поле В -> Извлечь В*: Канал кампании ```referral```
- *Вывод в -> Конструктор*: Канал кампании ```organic```
- ✔️ Поле А обязательно для заполнения
- ✔️ Поле Б обязательно для заполнения
- ✔️ Перезаписать поле вывода
- ▢ С учетом регистра


### Замена «yandex.ru/referral» на «yandex/organic»-2

- Название фильтра ```Замена «yandex.ru/referral» на «yandex/organic»-2```
- Тип фильтра: ```Пользовательский``` -> ```Расширенный```
- *Поле A -> Извлечь A*: Источник кампании ```^yandex\.ru$```
- *Поле В -> Извлечь В*: Канал кампании ```organic```
- *Вывод в -> Конструктор*: Канал кампании ```yandex```
- ✔️ Поле А обязательно для заполнения
- ✔️ Поле Б обязательно для заполнения
- ✔️ Перезаписать поле вывода
- ▢ С учетом регистра

Готово.