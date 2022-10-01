from django.urls import path
from . import views

urlpatterns = [
    path('response_csv/', views.response_csv),
]