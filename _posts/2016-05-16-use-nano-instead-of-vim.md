---
layout: post
title: Как использовать по умолчанию nano вместо vim
comments: false
category: bash
tags: bash, nano
---

If you use bash on macOS, this is easiest done by editing your ```~/.bash_profile``` file and adding the two lines

```bash
export EDITOR=nano
export VISUAL="$EDITOR"
```

