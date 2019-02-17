"""URL Configuration"""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from dataviz.views import APIPopulationView, APIEconomieView, APIMenagesView, GetDetailAPIMenagesView, LoginView, TerritoryChoice, ChartRender

urlpatterns = [

    path('', views.home, name='home'),

    path('login', LoginView.as_view(), name='login'),

    path('choice', TerritoryChoice.as_view(), name='choice'),

    path('board', views.board, name='board'),

    path('socio_demo/<user_input>/', ChartRender.as_view(), name='socio-demo'),

    path('api/population/data', APIPopulationView.as_view()),
    path('api/economie/data', APIEconomieView.as_view()),
    path('api/menages/data', APIMenagesView.as_view()),
    path('api/menages/data/<str:codgeo>', GetDetailAPIMenagesView.as_view()),
    path('api/menages/data/<user_input>', APIMenagesView.as_view()),
]



