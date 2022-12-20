from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    # поле для хранения произвольного текста
    text = models.TextField()
    # поле для хранения даты и времени
    pub_date = models.DateTimeField(auto_now_add=True)
    # поле, в котором указывается ссылка на другую модель
    author = models.ForeignKey(
            User, on_delete=models.CASCADE,
            related_name='posts')
    # чтобы можно было сослаться на Group
    group = models.ForeignKey('Group', blank=True, null=True,
                              on_delete=models.CASCADE)


class Group(models.Model):
    # название группы
    title = models.CharField(max_length=100)
    # уникальный адрес группы, часть URL
    slug = models.SlugField()
    # текст, описывающий сообщество
    description = models.TextField()

    def __str__(self):
        '''при печати объекта модели Group выводится поле title'''
        return self.title
