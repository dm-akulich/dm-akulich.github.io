---
layout: post
title: Java. Типы данных и алгоритмы
comments: False
category: java
tags: java
---

## 1. DATA TYPES

1. Boolean - true/false
2. Integer - whole number
3. Float/double - floating poiint
4. Char, string - symbol/string
5. Array
6. Map/Dictionary - associative array, key-value pairs
7. Queue/Stack (очереди и стеки) 

Переменная в программировании - некая сущность, которая имеет типа данных и значение. 

```
DataType variableName = value
```

```java
int number = 5
boolean isEven = false
String name = "Nixon"
```

```java
package com.company;

public class Main {

    public static void main(String[] args) {
        int number; // объявление переменной
        number = 7; // присваивание значения
	System.out.println(number);
    }
}
```

## NUMBERS

Как целые числа хранятся и записываются в приграммировании

Целые числа INT32 - их просто переводить в двоичную и обратно. Используются 32 бита. 2^31 - max

byte - 127 максимальное число 

```java
byte number_2 = 127;
```

Добрные числа.
особенность в том, что м ывсегда теряем какую-то точность.

$$ Number = m*n^p $$ 

Есть стандарты точности.

float - содержит 32-х битное число

double - повышенная точность. (64бит)

```java
package com.company;

public class Main {

    public static void main(String[] args) {
        double speed = 1;
        double divide = 3;
	System.out.println(speed/divide);
    }
}
>>> 0.3333333333333333
```

### Array

Array - набор однотипных элементов.

В java нельзя изменить размер массива, но есть и динамические массивы. В java есть конструкция list.

```java
package com.company;

public class Main {

    public static void main(String[] args) {
        int[] array_1 = {2, 4, 2, 5};
        array_1[3] = 7;
        System.out.println(array_1[3]);
    }
}
```

### Char и String

Char - для одного символа. Char это 16bit, которые хранят юникодовский код для хранения символа. Приметивный тип данных.
String - массив чаров.

```java
package com.company;

public class Main {

    public static void main(String[] args) {
        char letter = 'S';
        String my_sting = "Hello World";
        System.out.println(my_sting);
    }
}
```

### Map/Dictionary и Queue/Stack

Map - ассоциативный массив с ключами-значениями.

- Queue - First in First Out - очередь. То что добавляем идет в конец, то что забираем они находятся в начале очереди.
- Stack - First in Last Out - стек, типа колода карт. Удобен для хранения данных, если нужно положить элемент и потом быстро его забрать.



## OPERATORS

- ```--``` и ```++``` - Операторы инкремента и декремента. Увеличивают на единицу.
- ```+```, ```-```, ```*```, ```/```, ```%``` - 
- ```==```, ```!=``` - 
- ```&&```, ```||``` - 
- ```>```, ```<```, ```>=```, ```<=``` - 

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int number = 7;
        number++;
        System.out.println(number);
    }
}
>>> 8
```


```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int number = 7;
        int divide = 3;
        int result = number / divide;
        System.out.println(result);
    }
}
>>> 2
```

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int number = 7;
        int divide = 3;
        float result = number % divide;
        System.out.println(result);
    }
}
>>> 1.0
```

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        double number = 7;
        double divide = 3;
        double result = number / divide;
        System.out.println(result);
    }
}
>>> 2.3333333333333335
```

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        double number = 7;
        double divide = 3;
        boolean result = number == divide;
        System.out.println(result);
    }
}
>>> false
```

## Control Flow Statement

**Управляющие конструкции**

- if-then-else
- switch
- while, do-while
- for
- break, continue, return


```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int a = 7;
        int b = 3;
        if (a <= b) {
            System.out.println("a <= b");
        } else {
            System.out.println("a > b");
        }
    }
}
>>> a > b
```

### swith

Помогает, когда нужно комбинировать несколько if'ов.

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int monthNumber = 3;

        switch (monthNumber) {
            case 1:
                System.out.println("Jan");
                break; 
            case 2:
                System.out.println("Feb");
                break; // Если это номер 2, то выведи на печать и дальше не иди.
            case 3:
                System.out.println("Mar");
                break;
            case 4:
                System.out.println("Apr");
                break;
            case 5:
                System.out.println("May");
            default:
                System.out.println("Can't find the month");
        }
    }
}
>>> Mar
```

### while/for

#### WHILE

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int limit = 10;
        int currentNumber = 0;
        while (currentNumber < limit) {
            System.out.println(currentNumber);
            currentNumber++;
        }
    }
}
>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
```

Немного другая конструкция с ```do```:

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int limit = 5;
        int currentNumber = 0;
        do {
            currentNumber++;
            System.out.println(currentNumber);
        } while (currentNumber < limit);
    }
}
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
```

#### FOR

Можно задать конкретно количество итераций.

Обычно в круглых скобках три элемента. 

1. **Инициализация**. Можем инициализировать счетчик
2. **Условие прерывание цикла**. Будет выполняться, пока ```true```.
3. **Что делать, когда цикл пройдет круг**.

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }
    }
}
```

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int[] array = {2, 9, 9, 7};
        for (int i = 0; i <= 3; i++) {
            System.out.println(array[i]);
        }
    }
}
>>> 2
>>> 9
>>> 9
>>> 7
```

#### BREAK, CONTINUE, RETURN

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int[] array = {2, 9, 4, 7};
        for (int i = 0; i < 3; i++) {
            System.out.println("Cycle #" + i + " start");
            System.out.println(array[i]);
            if (array[i] == 4) {
                System.out.println("Found 4!");
                break;
            }
            System.out.println("Cycle #" + i + " end");
        }
    }
}
>>> Cycle #0 start
>>> 2
>>> Cycle #0 end
>>> Cycle #1 start
>>> 9
>>> Cycle #1 end
>>> Cycle #2 start
>>> 4
>>> Found 4!
```

- ```continue``` означает, что мы пропускаем все, что будет дальше в цикле и идем на следующий круг.
- ```return``` цикл прервется. Штука серьезнее ```break```. ```return``` полностью завешает работу текущего метода.



## FUNCTIONS

Функция - некая сущность, которая будет хранить в себе алгоритм и имеет удобный интерфейс передачи данных внутрь и возврат наружу и можем ее вызывать, когда нам нужно.

У функции есть тип данных, который она возвращает, есть имя функции и тип данных, который она принимает.

```java
double getAverageValue(int[] array) {
}
// void - функция ничего не возвращает.
void print(int[] array){
    
} 
double sum(int a, int b) {

}
```

Вывод массива в консоль с помощью функции

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        int[] array = {2, 9, 4, 7};
        printArrayToConsole(array);
        }
        static void printArrayToConsole(int[] arrayToPrint) {
            for (int i = 0; i < arrayToPrint.length; i++) {
                System.out.println(arrayToPrint[i]);
            }
        }
    }


>>> 2
>>> 9
>>> 4
>>> 7
```

**Сумма двух чисел**

```java
package com.company;
public class Main {
    public static void main(String[] args) {
        double sum = 0.0;
        sum = sumDouble(1.0, 2.0);
        System.out.println(sum);
        }

        static double sumDouble(double a, double b) {
            double sum = a + b;
            return sum;
        }
    }

>>> 3.0
```

### Big O notation

Сложность алгоритмов.

<img src="/assets/img/2020-11-07-java_data_types_and_algoritms/1.png">

Разные алгоритмы дают разную сложность.

Допустим Bubble Sort $$ O(n^{2}) $$. Если нам нужно отсортировать 100 элементов, то мы получим 10 000 операций. 




