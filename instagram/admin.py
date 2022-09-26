from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

@admin.register(Post) #장식자 문법으로 표현
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] #디스플레이에 출력할 컬럼 지정
    list_display_links = ['id','message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

