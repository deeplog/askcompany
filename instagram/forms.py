import re

from django import forms
from .models import Post

# 모델 Form  설계
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["message", "photo", "tag_set", "is_public"]  # 이 항목에 대해서만 유효성 검사

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if message:
            message = re.sub(r"[a-zA-Z]+", "", message)
        return message
