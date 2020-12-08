---
layout: post
category: django
title: 'Пагинация'
---



```python
# views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # По 3 статьи на каждой странице.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
        exceptPageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html', {'page': page, 'posts': posts})
```

В папке templates/ приложения blog создайте новый файл pagination.html. Добавьте в него следующий фрагмент кода:

```html
<div class="pagination">
  <span class="step-links">
    {#% if page.has_previous %#}
    <a href="?page={#{page.previous_page_number}#}">Previous</a>
    {#% endif %#}
    <span class="current">
      Page {#{ page.number }#} of {#{ page.paginator.num_pages }#}.
    </span>
    {#% if page.has_next %#}
    <a href="?page={#{ page.next_page_number }#}">Next</a>
    {#% endif %#}
  </span>
</div>
```

В этот шаблон необходимо передать объект Page для отображения ссылок на
предыдущую, текущую и следующую страницы, а также общее количество объектов. Давайте вернемся в шаблон ```blog/post/list.html``` и подключим ```pagination.
html``` в самом низу блока ```{#% content %#}```:

```HTML
{#% block content %#}
 {#% include "pagination.html" with page=posts %#}
{#% endblock %#}
```

Так как страница Page передается в шаблон статей под именем posts, подключаем шаблон постраничного отображения, указав, чему будет равен параметр
page. Можно применять такой способ для повторного использования блока постраничного отображения на различных страницах со списками разных объектов.
