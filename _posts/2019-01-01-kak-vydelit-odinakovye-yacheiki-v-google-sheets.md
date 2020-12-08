---
layout: post
category: other
title: 'Как подсветить одинаковые ячейки в google sheets'
tags: google-sheets
---


- выделили диапазон
- кликнули "формат"
- условное форматирование
- форматирование ячеек "Ваша формула"
- вставили формулу ```=AND(NOT(ISBLANK(A1)); COUNTIF($A$1:$F; "=" & A1) > 1)```
- магия
