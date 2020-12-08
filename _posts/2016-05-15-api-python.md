---
layout: post
category: python
title: 'API Python'
---

Задача: вывести из сервиса OpenWeatherMap название города и температуру.

```python
import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q':'Minsk',
    'appid': '6fa21b0028024c3de7c7ca43d3c45846',
}
# api_key = "6fa21b0028024c3de7c7ca43d3c45846"
res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers["Content-Type"])
data = res.json()
print(data["main"]["temp"])
# print(res.json())


>>> 200
>>> application/json; charset=utf-8
>>> 275.15
```

Потому что неправильный API KEY