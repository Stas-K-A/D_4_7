from django_filters import FilterSet, DateTimeFilter
from .models import News
from django.forms import DateTimeInput

# Создаем свой набор фильтров для модели News.
class NewFilter(FilterSet):
    # Поиск новостей от указанной до текущей даты
    added_after = DateTimeFilter(
        field_name='date_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},),
        )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = News
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по содержанию в заголовке и категории
           'title': ['icontains'],
           'newsCategory': ['exact'],
       }
