from django.contrib import admin
from .models import News, Category, NewsCategory

admin.site.register(News)
admin.site.register(Category)
admin.site.register(NewsCategory)
