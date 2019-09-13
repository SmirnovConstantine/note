from django.urls import path
# Импортируем стандартный представления входа и выхода
from django.contrib.auth.views import LogoutView, LoginView

from .views import RegisterView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # путь для  входа на сайт
    path('logout/', LogoutView.as_view(), name='logout'),  # путь для выхода с сайта
    path('register/', RegisterView.as_view(), name='register'),  # путь для регистрации на сайте
]
