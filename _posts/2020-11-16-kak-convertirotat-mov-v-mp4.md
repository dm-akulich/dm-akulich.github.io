---
layout: post
title: Как конвертировать MOV в MP4 через терминал
comments: False
category: bash
tags: bash
---

Необходимо использовать утилиту [http://ffmpeg.org/download.html](http://ffmpeg.org/download.html)

Once you have it installed, just issue the command in Terminal:

```bash
ffmpeg -i input.mov output.mp4
```

Можно еще добавить норм алиас 

```bash
alias convert="ffmpeg -i"
```





