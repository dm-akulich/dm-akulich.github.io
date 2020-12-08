---
layout: post
category: bash
title: 'Bash. Переменные, ветвление, циклы'
---

Переменная в Bash может состоять из:

- буквы, цифты, _. Не может начнаться с цифры
- значение переменной - буквы цифтры отдельыне символы

Запись и перезапись значения

<имя> = <значение>

```bash
path =~/Docs
```

Чтение:

```bash
$<имя> или $<значение> 
```

```bash
path2=$path/file.txt  #path2=~/Docs/file.txt
echo 'Path is $path2' #Path is ~/Docs/file.txt
```

```bash
#!/bin/bash

dir_path=~/Documents/
echo "My variable is $dir_path"
```

Bash разделяет понятие ' и "

Если мы используем " , то конструкция ```echo "$var2"``` выведет значение var2 - **значение переменной**. Но если перед долларом стоит обратный слэш, получится стока echo ```echo "\$var2"```

Если мы используем ' , то конструкция ```echo '$var2'``` выведет просто $var2 - **просто строка**

## Ветвление
Синтаксис:

```bash
if [[ условие ]]
then
	#действия, если условие верное
fi #означает оконсание условия
```

Условия (строки):

```bash
-z <строка> #строка пуста
-n <> #строка не пуста
<стр1> == <стр2> #строки равны
<стр1> != <стр2> #строки не равны
```



```bash
var1='Hello'
var2='Hello'
if [[ $var1 == $var2 ]]
then
	echo "Переменные равны"
fi
```

Сравниваать можно и числа:

**Условия[числа(строки)]:**

<число/строка> операция <числов/строка>


```
-eq, (==) #равно
-ne, (!=) #не равно
-lt, (<) #меньше
-le, #меньше или равно
-gt, (>) #больше
-ge, #больше или равно
```

**Условия (файлы):**

```bash
-e <путь> #путь существует
-f <путь> #это файл
-d <путь> #это директория
-s <путь> #размер файла блольше 0
-x <путь> #файл исполняемый
```

**Условия (логические):**

```bash
! #Отрицание логического выражения
&& #Логическое "И"
|| #Логическое "ИЛИ"
```

```bash
echo "Hi!"
if [[ $# -lt 2]] #проверяем, что количество аргументов меньше 2-х
then
	echo "You should at least two arguments!"
	exit
fi

if [[ !(-e $1) || (-f $1) ]] #проверяем НЕ существует ли путь $1 ИЛИ проверяем $1 НЕ является файлом
then
	echo "file $1 doesn't exist or is not a file"
	exit
fi

cp $1 $2
echo "Copied $1 to $2"

```



## Ветвление: альтернативы
### ELSE
Синтаксис:

```bash
if [[ условие ]]
then
	#действие, если истинно
elif
	#действие, если условие 1 ложно
else
	#действие, если ложно 1 и 2 условия
fi
```



Пример

```bash
if [[ -f $1 ]] 
then
  echo "Removing file"
  rm $1
elif [[ -d $1 ]]
then
  echo "Removing dir"
  rm -r $1
else
  echo "Can't remove $1"  
fi
```

```

### CASE ... IN
Синтаксис:

```bash
case переменная in
знач1)
	#действия, если переменная==знач1
	;;
знач2)
	#действия, если переменная==знач2
	;;
*)
	#действия, если переменная не равна не одному из вариантов
esac
```

Пример:

```bash
if [[ $# -ne 2 ]] 
then
  echo "You should specify exactly two arguments!"
else  
  case $1 in
    1)
      echo "Creating file $2"
      touch $2
      ;;
    2)
      echo "Creating dir $2"
      mkdir $2
      ;;
    *)
      echo "Wrong value!"
  esac
fi
```



## Циклы

Синтаксис:

### FOR

```
for переменная in список_значений #значения нужно указывать черел пробел
do
	#действия, каждый раз переменная
	#принимает следующее значение
	#из списка
done

break #прервать
continue #перейти на следующее значение
```


```bash
for i in 1 2 3 4 5
do
  file_name=file${i}.txt
  if [[ -e $file_name ]]
  then
    continue
  fi
  echo "Creating file $file_name"
  touch $file_name
done
```


### WHILE 

**Синтаксис:**

```
while [[ условие ]]
do
	#действия, пока условие истинно
done
	
```

```read``` переменная
	записать введенное пользователем значение в переменную



Пример:

```bash
#!/bin/bash

again=yes 
while [ "$again" == "yes" ] 
do
  echo "Please enter a name:"
  read name
  echo "The name you entered is $name"

  echo "Do you wish to continue? (yes/no)"
  read again
done
```