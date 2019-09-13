from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    """ Создание представления для регистрации пользователя """
    form_class = UserCreationForm  # стандартная форма для создания пользователя
    template_name = 'user/register.html'  # путь до шаблона регистрационной формы

