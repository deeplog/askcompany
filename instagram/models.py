from django.db import models


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d') #upload_to 옵션을 지정해서 파일을 상세 폴더로 분기함
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체에 대한 문자열 제공
    def __str__(self):
         return f"{self.message}"

    def message_length(self):
        return len(self.message)

    class Meta:
        ordering = ['-id']

    message_length.short_description = '메세지 글자수'

