---
layout: post
title: 'Асинхронное и многопоточное программирование в Python. Немного про GIL '
category: python
---

Очень круто про ```threading``` написано <a href="https://www.youtube.com/watch?v=Ad5fHlFHbOg">тут</a>

# 1. Многопоточное программирование 

**Основные понятия**:
- Процесс - это наша запущенная программа, которая работает и выполняет свои вычисления, а может быть чего-то **ждет**, например, данных из сети. В Свою очередь **процессы состоят из потоков**.
- Потоки - составляющие процесса, которые выполняются в рамках данного процесса. В рамках одного процесса выполняется как минимум один поток. В случае многопоточной программы это несколько потоков. То есть процесс для потоков является как бы группировкой.
- Блокировки - для синхронизации нескольких потоков необходимы **блокировки (события)**. Они нужны на случай, если один поток будет ожидать каких-либо событий, которые должны вызваться из другого потока.
- Многопоточная программа

<img src="/assets/img/2020-05-24-async-and-miltistream-prog/1.png">

**Цветами** выше показаны работающие подзадачи, например, поиск наибольшего числа в массиве и перебор значений в списке с целью его перемножения на 2 и получения результата.

**Белым** обозначены простои или ожидания вввода и вывода, будь то ожидание массива с сервера или из файла. На пикче видно, что программа имеет как бы два состояния.

Если две части алгоритма никак не связаны друг с ддругом, было бы логично вычислить их параллельно: в двух потоках. Останется только, потом их синхронизировать в один поток.

<img src="/assets/img/2020-05-24-async-and-miltistream-prog/2.png">

На пикче мы запускаем три потока независимых вычислений.

<img src="/assets/img/2020-05-24-async-and-miltistream-prog/3.png">

Python будет выполнять вычисление первого потока с блокировкой второго и третьего потоков. Так как перед получением управления он заблокирует mutex, который не позволит захватить двум другим потокам. То есть это некоторая блокировка, которую можно захватить один раз.

И до момента освобождения этой блокировки, никто другой не может ее использовать, получается, что мы вынуждены будем ждать завершения какого-ьто короткого вычисления от первого потока.

Потоки переключаются между собой последовательно и отдают возможность выполнения другому потоку. 

Такое поведение обусловлено GIL

<img src="/assets/img/2020-05-24-async-and-miltistream-prog/4.png">

GIL решает следующие задачи:

- Решает проблемы с разделяемой памятью и устранением ошибок доступа к одному и тому же участку памяти одновременно. 

<img src="/assets/img/2020-05-24-async-and-miltistream-prog/5.png">

В стандартной библиоеке есть модули для написания многопоточных программ.

# Модуль ```concurrent.future```

В основном многопоточная программа не даст прироста производительности из-за GIL, но можно реализовать многопроцессорную программу, где будет несколько GIL.

Данный модуль реализует Pull Executor. Мы можем епго использовать чтобы распараллелить процессы.



