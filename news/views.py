"""Standard library imports"""

# Django imports
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from news.models import Article, Category, CategoryToPost

def index(request):
    return render(request, 'index.html', {})

# def articles(request):
#     return render(request, 'home_news.html', {Article.objects.all().order_by('publication_date')[0:5]})


class ArticlesPage(TemplateView):
    template_name = "home_news.html"

    def article_list(self, request):
        queryset = Article.objects.order_by('publication_date')[:5]
        context = {"articles": queryset}
        return render(request, self.template_name, context)


def test(request):
    queryset = Article.objects.order_by('publication_date')[:5]
    context = {"articles": queryset}
    return render(request, "home_news.html", context)