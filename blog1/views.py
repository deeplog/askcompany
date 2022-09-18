from django.shortcuts import render
from .models import Post

#어떤 요청이 오면 호출되는 함수를 views에 정리한다.
def post_list(request):
    qs = Post.objects.all() #QuerySet
    #render 함수의 인자는 3개이다.
    return render(request, 'blog1/post_list.html',{
        'post_list': qs,
    })