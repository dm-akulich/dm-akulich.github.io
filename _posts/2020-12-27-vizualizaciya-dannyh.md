---
layout: post
title: Визуализация данных
comments: False
category: python
tags: python
---

# Визуализация с matplotlib

```python
import pandas as pd
import numpy as np
from numpy.random import exponential
%matplotlib inline

df = pd.DataFrame({'x': range(20), 'y': exponential(10,20)})
df.y.hist()
```

<img src="/assets/img/2020-12-27-vizualizaciya-dannyh/1.png">


# Расширенная визуализация с matplotlib



# Визуализация с pandas



# Интерактивная визуализация с plotly



