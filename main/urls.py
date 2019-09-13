from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('note/add/', NoteAdd.as_view(), name='note_add'),  # путь для добавления заметки
    path('note/<int:pk>/', notedetailview, name='note_detail'),  # путь для вывода заметок
    path('about/', about, name='about'),  # путь для вывода страницы about us
    path('', index, name='index'),  # путь для вывода страницы index

]
