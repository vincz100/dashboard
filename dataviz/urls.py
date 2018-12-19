from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from dataviz.views import UserChoice, ChartData, TerritoryChoice, LoginView

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('login', LoginView.as_view(), name='login'),

    path('choice', TerritoryChoice.as_view(), name='choice'),

    path('board', views.board, name='board'),

    path('socio_demo/<userinput>/', UserChoice.as_view(), name='socio-demo'),

    path('api/chart/data', ChartData.as_view()),

]



