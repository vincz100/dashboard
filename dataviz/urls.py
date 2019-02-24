"""URL Configuration"""

from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from dataviz.views import APIPopulationView, GetDetailAPIPopulationView, APIEconomieView, APIMenagesView, GetDetailAPIMenagesView, LoginView, TerritoryChoice, ChartRender

urlpatterns = [

    path('', views.home, name='home'),

    path('login', LoginView.as_view(), name='login'),

    path('choice', TerritoryChoice.as_view(), name='choice'),

    path('board', views.board, name='board'),

    path('socio_demo/<codgeo>/', ChartRender.as_view(), name='socio-demo'),

    path('api/population/data/', APIPopulationView.as_view()),
    path('api/population/data/<codgeo>/', GetDetailAPIPopulationView.as_view()),
    # url(r'api/population/data/(?P<codgeo>\d+)/$', GetDetailAPIPopulationView.as_view(), name='api-population'),

    path('api/economie/data/', APIEconomieView.as_view()),

    path('api/menages/data/', APIMenagesView.as_view()),
    path('api/menages/data/<codgeo>/', GetDetailAPIMenagesView.as_view()),
    # path('api/menages/data/<user_input>', APIMenagesView.as_view()),
]



