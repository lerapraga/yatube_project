# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница блога')


def group_posts(request, slug):
    return HttpResponse('Страница замечательных сообществ')
