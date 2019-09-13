from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.http import HttpResponseBadRequest

from .models import Note
from .forms import NoteForm
from .utils import work_pars


def index(request):
    """ Выводит страницу index.html """
    work_pars()
    return render(request, 'main/index.html')


@login_required
def about(request):
    """ Выводит страницу about, для зарегистрированных и вошедших пользователей """
    return render(request, 'main/about.html')


@login_required
def notedetailview(request, pk):
    """ Вывод всех заметок для определенного пользователя. Для зарегесрированного и вошедшего на сайт """
    note = Note.objects.filter(user=request.user)
    context = {'note': note}
    return render(request, 'main/note_detail.html', context)


class NoteAdd(LoginRequiredMixin, CreateView):
    """ Создание отображения страницы для добавления пользователем, заметок. """
    form_class = NoteForm
    template_name = 'main/note_add.html'

    def get_initial(self):
        # присваивает полю user в модели Note текущего пользователя
        return {'user': self.request.user.id}

    def form_valid(self, form):
        # проверка валидности формы
        if self.request.method == 'POST':
            return super().form_valid(form)
        else:
            preview = Note(url=form.cleaned_data['url'])
            ctx = self.get_context_data(preview=preview)
            return self.render_to_response(context=ctx)
        return HttpResponseBadRequest()



