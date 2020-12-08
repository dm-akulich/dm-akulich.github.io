---
layout: post
category: django
title: 'Сохранение данных из формы в БД'
---

**models.py**

```python
# appname/models.py
class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
```

**forms.py**

```python
# appname/forms.py
from django import forms
from .models import Subscribers

class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Subscribers
        exclude = ('',)
```

**views.pyь**

```python
# appname/views.py
from .forms import SubscribersForm

def LandingDefView(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_url')
    else:
        form = SubscribersForm()

    context = {'form': form,}
    return render(request, 'appname/index.html', context=context)
```

**admin.py**

```python
# appname/admin.py
from .models import Subscribers

@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
```

**index.html**

```html
# templates/appname/index.html
<form action="/" method="post">
    {#% csrf_token %#}
    {#{ form.as_p }#}
    <input type="submit" value="Submit">
</form>
```
