---
layout: post
title: Относительный импорт 
comments: False
category: python
tags: python
---

Исчточник https://napuzba.com/a/import-error-relative-no-parent

Ошибка возникает при попытке, когда нужно, будучи в дочернем подуле, испортировать что-то из родительского.

```
# Project Directory
project
 ├── config.py
 └── package
     ├── __init__.py
     └── demo.py
```

The ```config.py``` contains some variables which want to access in ```demo.py```. You decide to use relative import to achieve this simple task. 

```python
# project/config.py
count = 5
```

```python
# project/package/demo.py
from .. import config
print("The value of config.count is {0}".format(config.count))
```

When we invoke the demo script, we encounter the following error: 

```
/project>python package/demo.py
 Traceback (most recent call last):
   File "package/demo.py", line 1, in <module>
     from .. import config
 ImportError: attempted relative import with no known parent package
```

## How to fix

Let's change directory structure and create a new script

- First, create a new directory named ```new_project```
- Move the ```project``` directory to ```new_project```
- Create a new empty ```__init__.py``` inside the root directory - this will make the directory to a package.
- Create main.py in ```new_project``` directory

**The project directory**

```
new_project
 ├── main.py
 └── project
     ├── __init__.py
     ├── config.py
     └── package
         ├── __init__.py
         └── demo.py
```

```python
# new_project/main.py
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import project.package.demo
```