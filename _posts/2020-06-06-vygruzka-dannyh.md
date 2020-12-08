---
layout: post
title: Выгрузка данных. Как устроен GA. Core Reporting API и Query Explorer, Add-on Google Spreadsheet, другие способы выгрузки
comments: true
category: Web-analytics
tags: google-analytics
---

### Как устроен GA

<img src="/assets/img/2020-06-06-vygruzka-dannyh/1.png">

Коллекции. Сначала сюда собираются все данные 
Конфигурации это наши view и тп

**Подробнее это выглядит так**

<img src="/assets/img/2020-06-06-vygruzka-dannyh/2.png">

Measurement Protocol - это можно сказать АПИ, через который мы уведомляем GA, о том, что что-то произогло.

Embed API не только вытаскивает данные, но и визуализирует их.

### Core Reporting API

- Выгрузка больше чем два параметра (или 5 в flat table)
- Можно грузить из нескольких views
- Автоматизация



