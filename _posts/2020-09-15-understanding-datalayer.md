---
layout: post
title: Understanding DataLayer
comments: true
category: Web-analytics
tags: gtm
---

DataLayer в GTM это объект JavaScript, где хранятся сведения, переданные с веб-сайта: информация о событиях или переменные.

Данные хранятся в виде пар "ключ-значение" . Их можно передавать в сторонние приложения, например GA, или использовать как триггеры для активации тегов.

Пары "ключ-значение" передаются на уровень данных двумя способами.

## Способ 1

Первый способ - подстановка значений в уровень данных во время загрузки страницы (pre-populated values in DataLayer).

Например, компания предлагает на сайте нессколько туристических пакетов для разных категорий и стран.

Добавим переменную уровня данных ```{{tripCategory}}```. Ее значение будет соответствовать предлагаемому на странице виду отдыха (походы, лыщи, дайвинг)

```javascript
{{tripCategory}}

<script>
dataLayer = [{
    tripCategory: 'hiking',
}]
</script>
```

Также можно добавить переменную ```{{tripLocation}}``` с направлением поездки - странца, город и т.п.

```javascript
{{tripCategory}}
{{triLocation}}

<script>
dataLayer = [{
    tripCategory: 'hiking',
    triLocation: 'Belarus',
}]
</script>
```

Чтобы показывать рекламу тем, кто уже смотрел туры определенной категории в ту или иную страну.

Создадим триггер на основе просмотра страницы. Укажем в нем, что переменные ```{{tripCategory}}``` и ```{{triLocation}}``` должны принимать значения ```'hiking'``` и ```'Belarus'``` соответственно. При выполении этих условий триггер активирует тег для показа объявлений о походах в Беларуси. Нажав на него, пользователь снова попадет на страницу, где можно купить такой тур.

Тег поулчит доступ к этим значениям и будет активирован при загрузке страницы, если код уровня данных размещен перед фрагментов кода контейнера.

## Способ 2

Второй способ - прямая передача значений с веб-страницы на уровень данных с помощью push-метода JavaScript.

Предположим, что на сайте есть корзина, в которую пользователи могут асинхронно добавлять туры, не обновляя страницу.

Веб-мастер может написать код JavaScript, который будет передавать информацию о выбранных турах на уровень данных.

```javascript
{{tripCategory}}
{{triLocation}}

<script>
dataLayer.push ({
    tripCategory: 'hiking',
    triLocation: 'Belarus',
})
</script>
```

Таким образом, данные будут собраны независимо от загружаемых со страницей тегов.

Обратим внимание, что переменная уровня данных не передаются на другие страницы. Для этого нужно написать специальный код.

# Collecting data using the Data Layer, variables, and events

## Pass static values into Custom Dimensions

You can use user-defined variables that collect static values specific to your website to create Custom Dimensions for more detailed analysis in Google Analytics.

To collect the hard-coded value "Trip Category" let's first create a user defined DataLayer variable that tells Tag Manager when to collect this information.

Select ```User-Defined Variables - New```. Set variable name ```tripCategory```. Choose Type ```Data Layer Variable```.

<img src="/assets/img/2020-09-15-understanding-datalayer/1.png">

Name - ```tripCategory```

Default Value - ```not set```

<img src="/assets/img/2020-09-15-understanding-datalayer/2.png">


We can create the "Trip Location" variable in the same fashion.

Now we'll need to add the Data Layer to the "Destinations" page of the website.

We'll leave the DataLayer empty, since we-re not directly hard-coding any values into it. Beacuse websete wants t ocollect the category and location of each vacetion package for their custom dimensions, their web developers can set up a "data layer push" method on the "Details" buttons.

<img src="/assets/img/2020-09-15-understanding-datalayer/3.png">

Using this method, website can add hard-coded variables for ```tripCategory``` and ```tripLocation```, setting them us as key-value pairs in the Data Layer. Now, when users click on the "Destinations" button, the Data Layer will ccapture the hard-coded trip category and location.

<img src="/assets/img/2020-09-15-understanding-datalayer/4.png">

```javascript
{tripCategory: 'hiking',
 triLocation: 'Belarus',}
```

But we still need to get that information from the Data Layer into Analytics.

Since we want to include "Trip Category" and "Trip Location" as custom dimensions, we'll need to set up the dimensions in Google Analytics. 

In Analytics clack "Admin", in Property click "Custom Definitions", then "Cutom Dimensions". then "New custom dimension", set up name as ```Trip Category```. Scope "hit", active.

<img src="/assets/img/2020-09-15-understanding-datalayer/5.png">

We can create our "Trip Location" dimension using the same steps.

Once we've created a dimension, Analytics will present us with a code snippet.

<img src="/assets/img/2020-09-15-understanding-datalayer/6.png">

Each snippet will have a dimension numder (index) that we'll need to enter in Tag Manager to map the Analytics "Page View" tag to the proper Custom Dimensions.

<img src="/assets/img/2020-09-15-understanding-datalayer/7.png">

Now that we've set up our Data Layer method and created our custom dimensions, we'll have to update our Google Analytics tag in tag Manager to process the Data Layer variables as the custom dimensions we just created.

Click "Tags" and copy GA Tag.

<img src="/assets/img/2020-09-15-understanding-datalayer/8.png">

<img src="/assets/img/2020-09-15-understanding-datalayer/9.png">

Then we'll rename the tag as ```... - Destination Button``` and configure it.

<img src="/assets/img/2020-09-15-understanding-datalayer/10.png">

Then select type "Event" and configure as we need. Set up Label Field with our vaeriable.

<img src="/assets/img/2020-09-15-understanding-datalayer/11.png">


Then set up Custom Dimension.

<img src="/assets/img/2020-09-15-understanding-datalayer/12.png">

Then click "Continue".

<img src="/assets/img/2020-09-15-understanding-datalayer/13.png">

Select the "Click Trigger". And configure trigger only for URL ```destination.html``` and button.

<img src="/assets/img/2020-09-15-understanding-datalayer/14.png">

<img src="/assets/img/2020-09-15-understanding-datalayer/15.png">

<img src="/assets/img/2020-09-15-understanding-datalayer/16.png">

Now let's view website in "Preview" mode.

When we click on the "Variables" tab in the Preveiw window we can see the Data Layer variable we set up, alung with the string for the variable.

<img src="/assets/img/2020-09-15-understanding-datalayer/17.png">

Now when we run a report in Google Analytics, we should be able to add the Custom Dimension and view daa by how website organises their trip categories and trip locations.


## Pass dynamic values into Custom Metrics

Tag Manager lets us pass dynamoc values such as revenue from website into Custom Metrics tha we can use in Google Analytics to analyze things like purschare behavior.

To set this up, let's create a user-defined Data Layer variable for "Trip Value".

Select Variables -> User-Defined Variables -> New -> Data Layer Variable

<img src="/assets/img/2020-09-15-understanding-datalayer/18.png">

Configure Variable name as "tripValues".

<img src="/assets/img/2020-09-15-understanding-datalayer/19.png">

Then select create variable.

<img src="/assets/img/2020-09-15-understanding-datalayer/20.png">

Next, we'll add the Data Layer code to the Trip Purschare "Thank You" page that passes the total trip value from the URL to the Data Layer.

<img src="/assets/img/2020-09-15-understanding-datalayer/21.png">

Now we can write some JavaScript code that extras the trip price from URL using a variable called tripPrice.

<img src="/assets/img/2020-09-15-understanding-datalayer/22.png">
c
Using this variable, we can then push the trip price to the Data LAyer object. When users complete a purschare, we should see the value of the purschare passed into the Data Layer as the ```tripValue``` variable we just created. We can confirm this by placing our container in Preview Mode and looking at the Data Layer status for the loaded page.

<img src="/assets/img/2020-09-15-understanding-datalayer/23.png">


We can set up a Custom Metric to collect the trip amount.

Custom Metrics are set up sililarly to Custom Dimensions.

<img src="/assets/img/2020-09-15-understanding-datalayer/24.png">

As wit hCustom Dimensions, Cunstom Metrics will present with an index number, that we'll use to map back to Tag Manager.

<img src="/assets/img/2020-09-15-understanding-datalayer/25.png">

Similar to our "Trip Category" and "Trip Location" dimensions, we'll have to update our Google Analytics tag within Tag Manager.

<img src="/assets/img/2020-09-15-understanding-datalayer/26.png">

Then click "Custom Metrics" and set up it.

<img src="/assets/img/2020-09-15-understanding-datalayer/27.png">

Then save tag.

Now that we've set up our Custom Metric and mapped it back to Tag Manager.

We can build a Custom report in Google Analytics to view the transaction data.

<img src="/assets/img/2020-09-15-understanding-datalayer/28.png">

<img src="/assets/img/2020-09-15-understanding-datalayer/29.png">
















