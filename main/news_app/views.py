from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import *
from .filters import NewFilter
from .forms import NewForm


class NewsList(ListView):
    model = News
    ordering = '-date_creation'
    context_object_name = 'News_make'
    template_name = 'news_app/news.html'
    paginate_by = 10


class NewsSearch(ListView):
    model = News
    ordering = ['title']
    template_name = 'news_app/news_search.html'
    context_object_name = 'search'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = News
    context_object_name = 'New'
    template_name = 'news_app/new.html'

class NewCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель новости
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.type = 'NW'
        return super().form_valid(form)


# Добавляем представление для изменения новости
class NewUpdate(UpdateView):
    form_class = NewForm
    model = News
    template_name = 'new_edit.html'

# Представление удаляющее новость.
class NewDelete(DeleteView):
    model = News
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news')


