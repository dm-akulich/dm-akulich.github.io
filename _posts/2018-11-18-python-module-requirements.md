---
layout: post
title: 'Python модуль requirements'
category: python
---

Прочитаем html из интернета

```python
from urllib import request

myUrl = "http://adv400.tripod.com/"

otvet = request.urlopen(myUrl)

mytext1 = otvet.readlines() # построчный вывод. Поэтому используем for

mytext2 = otvet.read()

print(otvet)

print(mytext2)

for line in mytext1:
	print(line)
```


Запрос в google с параметрами

```python
from urllib import request, parse
import sys

myUrl = 'http://www.google.com/search?'
value = {'q': 'Andesa Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

try:
	mydata = parse.urlencode(value)
	print(mydata)
	myUrl = myUrl + mydata
	req = request.Request(myUrl, headers=myheader)
	otvet = request.urlopen(req)
	otvet = otvet.readlines()
	for line in otvet:
		print(line)
except Exception:
	print("Error occuried during web request")
	print(sys.exc_info()[1]) # вывод только ошибки, а не всего лога
```


Скачаем файл из интернета

```python
from urllib import request
import sys

myUrl = "https://www.remeza.com/upload/medialibrary/2b0/fiac_direct_drive_1_5_1_8kw.png"

myFile = "/Users/dima/desktop/downloaded.png"

try:
	print("start download file = " + myUrl)
	request.urlretrieve(myUrl, myFile)
except Exception:
	print("Warning")
	print(sys.exc_info()[1])
	exit()

print("file downloaded and saved at " + myFile)
```