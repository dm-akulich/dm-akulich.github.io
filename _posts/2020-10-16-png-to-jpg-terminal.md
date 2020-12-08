---
layout: post
title: PNG в JPG в терминале
comments: true
category: bash
tags: bash
---

```bash
for i in *.png; do sips -s format jpeg $i --out /Users/dima/Desktop/img_jpg/$i.jpg;done
```

