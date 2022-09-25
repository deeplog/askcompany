from django.db import models


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

