---
layout: post
title: Схема событий для GTM
comments: true
category: Web-analytics
tags: google-analytics
---

**События**

**Пример пуша:** ```dataLayer.push({'event': 'autoEvent', 'eventCategory': '', 'eventAction': '', 'eventLabel: '', 'eventValue': '', 'eventNonInteraction': FALSE});```

Меняем только значения ключей eventCategory, eventAction, eventLabel, eventValue и eventNonInteraction согласно схеме ниже. Если значения нет – оставляем пустые кавычки.

Некоторые поля могут иметь динамическое значение: я его указывал в <скобках>

| Триггер |eventCategory |eventAction |eventLabel |	eventValue |eventNonInteraction |
| ----------- | ----------- | ----------- |----------- |----------- |----------- |
| Отправка формы регистрации           | Registration form       | Submit       |```<url>```       |       |FALSE       |
| Отправка заявки на консультацию      | Consultation Form       | Submit       |```<url>```       |       |FALSE       |
| Отправил сообщение/обратную связь      | Feedback form       | Submit       |```<url>```       |       |FALSE       |
| Нажатие на кнопку регистрации      | RegButton       | Click       |Top/Middle/Bottom       |       |FALSE       |
| Скролл до 25%      | Scroll Distance       | Percentage       |25%       |       |TRUE       |
| Скролл до 50%      | Scroll Distance       | Percentage       |50%       |       |TRUE       |
| Скролл до 75%      | Scroll Distance       | Percentage       |75%       |       |TRUE       |


