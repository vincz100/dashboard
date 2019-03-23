from . import views
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from news.views import ArticlesPage

urlpatterns = [
    path('front/articles/', ArticlesPage.as_view()),
]