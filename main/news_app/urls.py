from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>', NewDetail.as_view(), name='detail_new'),
    path('news/search', NewsSearch.as_view()),
    path('news/create/', NewCreate.as_view()),
    path('news/<int:pk>/edit/', NewUpdate.as_view()),
    path('news/<int:pk>/delete/', NewDelete.as_view()),
]