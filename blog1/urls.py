from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'), #매핑, 함수를 넘긴다. (일급함수 참고)
]