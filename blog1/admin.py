from django.contrib import admin
from .models import Post

#admin 페이지에 Post 임포트

admin.site.register(Post)