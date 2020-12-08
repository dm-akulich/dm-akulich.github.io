---
layout: post
title: 'Интересные задачки в python'
category: python
---


```python
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
```
