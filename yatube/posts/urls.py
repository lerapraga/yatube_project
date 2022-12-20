# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # главная страница
    path('home_posts/', views.index, name='home_posts'),
    # страница сообществ
    path('group/<slug:slug>/', views.group_posts, name='group_posts')
]
