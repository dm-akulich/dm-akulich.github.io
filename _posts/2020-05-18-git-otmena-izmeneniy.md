---
layout: post
title: 'git. Отмена изменений'
category: git
tags: git
---

# Отмена измений в директории

Допустим, у нас сейчас в репозитории лежит следующий код

```python
# func.py

print("Hello World")


def foo(x, y):
    return x * y


if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

```

Мы сделали какие-то изменения (удалили все что ```if __name__...```) и теперь хотим вернуть обратно.

```python
# func.py

print("Hello World")


def foo(x, y):
    return x * y


```


Посмотреть изменения можно с помощью команды ```git diff```

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/1.png">

Чтобы вернуть версию из репоитория воспользуемся командой ```git checkout -- func.py```. Два подчеркивания говорят Гиту, чтобы он оставался в текущей ветке.

Теперь файл прежний

```python
# func.py

print("Hello World")


def foo(x, y):
    return x * y


if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

```

# Отмена измений в буфере. Как отменять изменения, которые мы отправили в буфер.

Для начала изменим файл и отправим что-нибудь в буфер.

**Файл ДО изменений**

```python
# func.py
print("Hello World")


def foo(x, y):
    return x * y


if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

```

**Файл ПОСЛЕ изменений**

```python
# func.py
print("Hello World")


def foo(x, y):
    return x * y

def foo2():
    return print("another function")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

    foo2()
```

Эти изменения сейчас в рабочей директории, но они еще не в буфере.

Добавляем изменения в буфер ```git add func.py```. С помощью ```git status``` видим, что изменения были отправлены в буфер.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/2.png">

Теперь мы хотим отменить изменения, чтобы они опять стали **изменениями директории**. Такое может понадобиться если мы хотим объединить все наши изменения в один коммит.

Сейчас задача в том, чтобы **вывести этот один файл из буфера**, а остальные файлы (если они там есть) оставить. Для Этого воспользуемся командой ```git reset HEAD func.py```


*HEAD указывает на последний коммит наверху текущего бранча, который является основным бранчем (это наш текущий бранч)*

Посмотрим на последний коммит и вернесмся к тому, что было до этого (очень похоже на ```checkout```). ```checkout``` забирал файл из репозитория, здесь мы сбрасываем изменения в буфере, чтобы они были такими же как и эти.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/3.png">



Если мы что-то добавим в буфер, а потом не захотим этого там видеть, можно использовать ```git reset HEAD```

При этом файл все еще измененный.

```python
# func.py
print("Hello World")


def foo(x, y):
    return x * y

def foo2():
    return print("another function")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

    foo2()
```

# Отмена измений в репозитории. Как отменять коммиты (это уже сложнее)

У нас есть возможность изменить последний коммит, потому что от него пока что ничего не зависит. То есть мы можем изменить коммит, на который указывает **HEAD**. 

Добавим наш измененный ```func.py``` в репозиторий.

```python
# func.py
print("Hello World")


def foo(x, y):
    return x * y

def foo2():
    return print("another function")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)

    foo2()
```

С помощью комант ```add``` и ```commit```.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/4.png">


Посмотрим лог изменений с помощью ```git log```.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/5.png">

И тут мы понимаем, что это не совсем то, что мы хотели коммитить. Мы хотим, чтобы коммит был с кодом файла

```python
print("Hello World")


def foo(x, y):
    return x * y


if x > 3:
    print("More than 3")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)
```

Если мы сейчас посмотрим ```git status```, то увидим, что он нам предлагает сделать еще один коммит. А мы хотим это изменение добавить в последний коммит.


<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/6.png">

Мы можем отредактировать коммит, вставив изменение в буфер ```git add func.py```.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/7.png">

И использовать команду ```git commit --amend -m "initial commit"```.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/8.png">

**Посмотрим лог**

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/9.png">

*Таким образом можно и изменять сообщение коммита, если предыдущее не ок.*

# Отмена измений до каких-либо предыдущих коммитов (не последнего)

Git не позволяет прятать ошибки, мы можем сделать чекаут старого файла и сделать новый коммит.

Файл сейчас выглядит так.

```python
print("Hello World")


def foo(x, y):
    return x * y


if x > 3:
    print("More than 3")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)
```

Посмотрим лог. Допустим, мы хотим вернуться на состояние файла на момент коммита "initial"

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/10.png">

Для этого воспользуемся командой ```git checkout <hash> -- <filename>```

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/11.png">

Состояние файла теперь.


```python
print("Hello World")


def foo(x, y):
    return x * y


if __name__ == "__main__":
    x = foo(3, 2)
    print(x)
    
```

Посмотреть изменения можно с помощью ```git diff staged```

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/12.png">

Теперь можно сделать обычный коммит и это отменит изменения, которые были ранее.


# Отмена измений коммита целеком и полностью 

Посмотрим **Лог**

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/13.png">

Команда ```revert``` возьмет все изменения в коммите ```bug fuxed``` и уберет их. Таким образом, все что было добавлено - будет удалено, а все, что было удалено - будет добавлено.

Файл сейчас

```python
print("Hello World")


def foo(x, y):
    return x * y


if __name__ == "__main__":
    x = foo(3, 2)
    print(x)
```

Используем команду, указав SHA помледнего коммита.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/14.png">

Далее появится возможно изменить сообщение коммита.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/15.png">

Из гита выходим через ```:wq!```.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/16.png">

**Состояние файла теперь**

```python
print("Hello World")


def foo(x, y):
    return x * y


if x > 3:
    print("More than 3")

if __name__ == "__main__":
    x = foo(3, 2)
    print(x)
```



```git log``` теперь показывает, что мы перевернули предыдущий коммит.

<img src="/assets/img/2020-05-18-2020-05-18-git-otmena-izmeneniy/17.png">








