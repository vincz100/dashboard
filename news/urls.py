from . import views
from django.urls import path

from news.views import NewsPage

urlpatterns = [
    path('front/<lib_projet>/news/', NewsPage.as_view()),
]