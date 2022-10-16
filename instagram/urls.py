from django.urls import path, re_path, register_converter
from . import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)


register_converter(YearConverter, "year")
app_name = "instagram"  # URL Reverse에서 Name Spaece 역할을 함

urlpatterns = [
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    # path('archives/<int:year>/', views.archives_year), # path 사용하기
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year) # 정규식 사용하기
    # path(r'archives/<year:year>/', views.archives_year) #custom converter 사용하기
    path("archive/", views.post_archive, name="post_archive"),
    path("archive/<year:year>/", views.post_archive_year, name="post_archive_year"),
]
