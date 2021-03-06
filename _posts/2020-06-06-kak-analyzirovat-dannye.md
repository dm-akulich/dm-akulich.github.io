---
layout: post
title: Как анализировать данные в GA
comments: true
category: Web-analytics
tags: google-analytics
---

*Примечание*. это конспект курса со [Stepik](https://stepik.org/course/1878/syllabus)

## Зачем нужна веб-аналитика?

**Зачем нужна веб-аналитика?** Чтобы, основываясь на полных и достоверных данных, сделать что-то лучше.

## Процесс анализа

1. Зоны роста
2. Гипотеза
3. Эксперимент
4. Анализ результата
5. Внедрение


## Кому нужна веб-аналитика

Примеры метрик для контентных сайтов:

- Качество чтения (Глубина скролла + точное время) то есть фактически в GA пушится событие что человек так то взаимодейстовал с конентом
- Лайки, шеры и т.п. Сводим в одну метрику
- Группировака по авторам и категориям (создаем нужную нам структуру). Кого больше лайкают и тп
- Качество перелинковки

Для е-коммерс:

- Как человек взаимодействовал с карточкой товара

## Сегментация 

Например, мы можем сравнить две группы:

1. Молодые мужчины из Киева, которые были на продуктовой страницы IPhone 7 более 3 раз, пришли из соц. сетей, прочитали все комментарии, посмотрели видео-обзор и добавили товар в корзину; **И не купил** - и для этиг групп аудиторий можем делать ремаркетинг.
2. И те же, но женщины

Зачем сегментировать:

- Для формирования уникального предложения для каждого сегмента;
- Для повышения количества сделок в определенные дни / время;
- Для контекстного формирования акций для определенного сегмента.


<img src="/assets/img/2020-06-06-kak-analyzirovat-dannye/1.png"> 

*Пример кастомного отчета*. Мы можем надавить на самую конверсионную аудиторию и получить больше денег. Мужчины из Бучи, хороший пример **зон роста**.

**Сегментированные отчеты (с настройками) относительно конверсии**
- В какое время посещаемость и конверсия сайта самая высокая;
- Сколько времени люди проводят на сайте до совершения покупки;
- Какие дни самые конверсионные, а в какие продажи падают;
- Какие устройства аудитория использует чаще всего, какие устройства являются самыми конверсионными.

<img src="/assets/img/2020-06-06-kak-analyzirovat-dannye/2.png">
<img src="/assets/img/2020-06-06-kak-analyzirovat-dannye/3.png">

Как рассчитывается среднее время пребывания (сессии)?. 
Разница между первым и последним хитом

## Тестирование, KPI и гипотезы

1. Формируем гипотезу;
2. Определяем KPI;
3. Настраиваем аналитику;
4. Запускаем тест;
5. Анализируем результат.

Гипотезы для проверки:
- Прохождение сценария;
- Эффективность баннеров, акций, скидок;
- Какой ключевой посыл;
- Как количество отзывов на странице влияет на конверсию;
- Взаимодействия с фильтрами, качество взаимодействия;
- Влияет ли на конверсию просмотр видео (досмотр до середины или до конца);
- Что лучше работает – конкретное предложение или возможность выбора.

Примеры KPI:
- Прохождение сценария — точки прохождения;
- Эффективность баннеров, акций, скидок;
- Ключевой посыл;
- Как количество отзывов на странице влияет на конверсию;
- Взаимодействия с фильтрами, качество взаимодействия;
- Влияет ли на конверсию просмотр видео (досмотр до середины или конца);
- Что лучше работает – конкретное предложение или возможность выбора?

[Определение объема выборки](https://www.evanmiller.org/ab-testing/sample-size.html)

**Для порядка в GA**

Делим представления:

- Master View - Основное представление, исключаем нужные ip
- Test View - только для текстирования
- Raw Data View - сырые данные

- CPC View - только для контекста
- UX View - с целями для UX
- Content View - с целями для контента









