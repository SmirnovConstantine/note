from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class Note(models.Model):
    """ Создание модели заметок. Поле user будет заполняться из стандартной модели пользователя,
    и при удалении пользователя, связанные с ним записи тоже будут удаляться. Поле url, пользователь
    сможет добавить заметку, ввиде url-адреса. После добавления закладки, должен начинать работать
    парсер, который будет брать информацию с страницы и заносить её в поля title, description ,image """

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    url = models.URLField(max_length=8000, verbose_name='URL')
    title = models.CharField(max_length=300, blank=True, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(blank=True, null=True, verbose_name='Image')
    is_parse = models.BooleanField(default=False)

    def __str__(self):
        """ Строкое представление url в панели администратора """
        return self.url

    def get_absolute_url(self):
        """ Возращает указанный шаблон после добавления записи в БД """
        return reverse('main:index')
