from django import forms
from .models import Post

# 모델 Form  설계
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
