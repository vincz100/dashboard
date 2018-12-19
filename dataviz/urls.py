from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from dataviz.views import DataViz, ChartData, HomeView, LoginView

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('login', LoginView.as_view(), name='login'),

    path('choice', HomeView.as_view(), name='choice'),

    path('board', views.board, name='board'),

    path('socio_demo/', DataViz.as_view(), name='socio-demo'),

    path('socio_demo/api/chart/data/', ChartData.as_view()),
]



