from django import forms
from .models import News


# Модель формы для создания и редактирования новостей
class NewForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'text', 'type', 'slug']

