---
layout: post
category: django
title: 'Функция get_absolute_url'
---

Обычно используем в detail целях

Добавляем в модель

```python
# /blog_app/models.py
from django.shortcuts import reverse

class Post(model.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

```

Добавляем в views.py

```python
# /blog_app/views.py
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context=context)
```

Добавляем в шаблон

```html
<!-- /blog_app/views.py -->
{#% for posts in post %#}
<a href="{#{ post.get_absolute_url }#}" class="btn btn-primary">Go</a>
{#% endfor %#}
```
