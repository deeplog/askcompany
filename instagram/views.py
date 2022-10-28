from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    DetailView,
    ListView,
    ArchiveIndexView,
    YearArchiveView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import PostForm


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user  # 현재 로그인 User Instance
#             post.save()
#             messages.success(request, "포스팅을 저장했습니다.")
#             return redirect(post)  # 저장을 하고 이동이 되게 한다.
#     else:
#         form = PostForm()
#
#     return render(
#         request,
#         "instagram/post_form.html",  # 폼을 보여준다.
#         {
#             "form": form,
#             "post": None,
#         },
#     )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, "포스팅을 저장했습니다.")
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 작성자 Check Tip
#     if post.author != request.user:
#         messages.error(request, "작성자만 수정할 수 있습니다.")
#         return redirect(post)
#
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, "포스팅을 수정했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(
#         request,
#         "instagram/post_form.html",
#         {
#             "form": form,
#             "post": post,
#         },
#     )


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, "포스팅을 수정했습니다.")
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "포스팅을 삭제했습니다.")
#         return redirect("instagram:post_list")
#     return render(
#         request,
#         "instagram/post_confirm_delete.html",
#         {
#             "post": post,
#         },
#     )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = reverse("instagram:post_list") # 안됨

    # def get_success_url(self):
    #     return reverse("instagram:post_list") #됨

    success_url = reverse_lazy("instagram:post_list")  # 됨


post_delete = PostDeleteView.as_view()


# @login_required
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

# login_required 추천하는 방법
# @method_decorator(login_required, name='dispatch')
# class PostListView(ListView):
#     model = Post
#     paginate_by = 10


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100


# class PostListView(ListView):
#     model = Post
#     paginate_by = 100

post_list = PostListView.as_view()

# ListView 활용
# post_list = ListView.as_view(model=Post, paginate_by=10)


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


# post_detail = DetailView.as_view(model=Post)

# get_queryset 재정의
class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()

# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(
    model=Post, date_field="created_at", paginate_by=10
)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field="created_at", make_object_list=True
)
