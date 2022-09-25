from django.contrib import admin
from .models import Post

@admin.register(Post) #장식자 문법으로 표현
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] #디스플레이에 출력할 컬럼 지정
    list_display_links = ['id','message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    pass
