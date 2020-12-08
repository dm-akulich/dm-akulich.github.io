---
layout: post
title: 'Валидация формы в GA'
category: Web-analytics
tags: google-analytics
---

**Создаем тег** с типом отслеживания Событие, задаем **категорию**, например, ```form``` и **действие**, например, ```send```. Указываем настройки Google Analytics.

**Создаем триггер** и задаем ему настройки:

- Тип триггера: ```Клик - Все элементы```
- Условия активации триггера: тут создаем новую переменную, к условиям активации вернемся позже.

**Создаем новую переменную**

- Задаем имя переменной, например, ```GA_Валидация_формы```.
- Тип триггера: ```Собственный код javascript```

```javascript
 function (){
    var name = jQuery('#frm-question-FIO').val();
    var email = jQuery('#frm-question-PHONE').val();
    var tel = jQuery('#frm-question-EMAIL').val();
    var message = jQuery('#frm-question-MESSAGE').val();
    var emailReg = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
    var telReg = /^\+?[0-9()\- ]{7,20}$/;
    if(name.length > 0 && emailReg.test(email) && telReg.test(tel) && message.length > 0) {
       return true;
    } else {
       return false;
    }
 }
```

Кастомим код в зависимости от полей и привязываем к нужным ```id``` полей.

**Возвращаемся к триггеру**

Ставим условия активации триггера:
- Выбираем нашу только что созданную переменную ```'GA_Валидация_формы' равно true```
- Выбираем ```Click ID равно``` и ```id``` кнопки подтверждения, например, ```submit_FRM_CONTACTS```
 
Готово

