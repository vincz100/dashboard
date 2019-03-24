from django.urls import path, include
from django.shortcuts import render

from django.views.generic import TemplateView

from news.models import Article, Category, CategoryToPost

def index(request):
    return render(request, 'index.html', {})

# def articles(request):
#     return render(request, 'home_news.html', {Article.objects.all().order_by('publication_date')[0:5]})

class ArticlesPage(TemplateView):
    template_name = "home_news.html"

    def article_list(self, request):
        # queryset = Article.objects.get(id=1)
        queryset = Article.objects.order_by('publication_date')[0:5]
        context = {
            "articles": queryset
        }
        return render(request, self.template_name, context)