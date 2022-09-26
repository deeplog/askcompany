from django.shortcuts import render
from .models import Post

def post_list(reqeust):
    qs = Post.objects.all()
    q = reqeust.GET.get('q','') # q key가 있으면 가져오고, 없으면 ''
    if q:
        qs = qs.filter(message__icontains=q) # 필터링 기능 구현이 됨
        #instagram/templates/instagram/post_list.html
    return render(reqeust, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
        })