from django.urls import path, include
from django.shortcuts import render

from django.views.generic import TemplateView


class NewsPage(TemplateView):
    template_name = "home.html"

    def news_list(self, parameter_list):
        pass