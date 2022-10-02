from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post

# def post_list(reqeust):
#     qs = Post.objects.all()
#     q = reqeust.GET.get('q','') # q key가 있으면 가져오고, 없으면 ''
#     if q:
#         qs = qs.filter(message__icontains=q) # 필터링 기능 구현이 됨
#         #instagram/templates/instagram/post_list.html
#     return render(reqeust, 'instagram/post_list.html', {
#         'post_list':qs,
#         'q':q,
#         })

#ListView 활용
post_list = ListView.as_view(model=Post, paginate_by=10)


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk) # 포스트 하나를 얻는다.
#     # except Post.DoesNotExist: # DoesNotExist 예외 처리
#     #     raise Http404
#
#     post= get_object_or_404(Post, pk=pk) #예외처리 간단하게 하는 방법
#     return render(request, 'instagram/post_detail.html', {
#         'post':post,
#     })


#post_detail = DetailView.as_view(model=Post)

#get_queryset 재정의
class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")