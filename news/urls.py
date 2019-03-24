from . import views
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from news.views import index, ArticlesPage

urlpatterns = [
    path('front/', index),
    path('front/articles/', ArticlesPage.as_view()),
]