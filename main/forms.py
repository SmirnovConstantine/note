from django import forms
from django.contrib.auth import get_user_model

from .models import Note


class NoteForm(forms.ModelForm):
    """ Создание формы для добавления заметки, ввиде url-адреса """

    url = forms.URLField()
    user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=get_user_model().objects.all(), disabled=True)

    class Meta:
        model = Note
        fields = ('url', 'user', )
