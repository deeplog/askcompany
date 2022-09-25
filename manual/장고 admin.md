### django admin

* django.contrib.admin 앱을 통해 제공
* admin/ 을 통해 접근하면 어드민 페이지 이동
* 웹 UI 제공
* 서비스 초기에 관리 도구로 사용할때 활용
* End-User 서비스에 집중해서 관리

### admin에 등록하는 방법

```python
from django.contrib import admin
from .models import Item

# 등록법 1
admin.site.register(Item)
```

```python
# 등록법 2
class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register()
```

```python
# 등록법 3
@admin.register(Post) #장식자 문법으로 표현
class PostAdmin(admin.ModelAdmin):
    pass
```

```shell
> python manage.py shell
>>> from instagram.models import Post
>>> Post.objects.all()
>>> qs = Post.objects.all().filter(message__icontains='첫번째')
>>> print(qs.query)
```

모델 수정
```python
class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체에 대한 문자열 제공
    def __str__(self):
         return f"Custom Post object ({self.id})"

    def message_length(self):
        return len(self.message)

    message_length.short_description = '메세지 글자수'
```

django admin 화면 셋팅
```python
from django.contrib import admin
from .models import Post

@admin.register(Post) #장식자 문법으로 표현
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] #디스플레이에 출력할 컬럼 지정
    list_display_links = ['id','message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    pass
```

모델 적용
```shell
python manage.py makemigrations instagram
python manage.py migrate instagram
python manage.py showmigrations instagram
```
