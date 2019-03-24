from django.urls import path, include
from django.shortcuts import render

from django.views.generic import TemplateView

from news.models import Article, Category, CategoryToPost

def index(request):
    return render(request, 'index.html', {})

class ArticlesPage(TemplateView):
    template_name = "home_news.html"

    def article_list(self, parameter_list):
        queryset = Article.objects.all().order_by('publication_date')[0:5]
        context = {
            "articles": queryset
        }
        return render(request, self.template_name, context)