from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views
from news.views import index, article_list

urlpatterns = [
    path('front/', index),
    path('front/articles/', article_list)
]