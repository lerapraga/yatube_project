# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # главная страница
    path('', views.index),
    # страница сообществ
    path('group/<slug:slug>/', views.group_posts)
]
