from django.db import models
from django.shortcuts import reverse

# Описание модели - Категория новостей
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


# Описание модели - Новости
class News(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)
    newsCategory = models.ManyToManyField(Category, through='NewsCategory')

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOCES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    # Тип новости - статья или новостное сообщение
    type = models.CharField(max_length=2, choices=CATEGORY_CHOCES, default=NEWS)

    def get_absolute_url(self):
        return reverse('detail_new', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'


# Описание модели - Промежуточная таблица соответствия новости и ее категории
class NewsCategory(models.Model):
    newsThrough = models.ForeignKey(News, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)