from django.urls import path

from . import views
from dataviz.views import Population, get_data, ChartData, HomeView

urlpatterns = [
    
    path('', views.home, name='home'),

    path('login', HomeView.as_view(), name='login'),

    path('board', views.board, name='board'),

    path('socio_demo/', Population.as_view(), name='socio-demo'),

    path('api/data/', get_data, name='api-data'),
    path('socio_demo/api/chart/data/', ChartData.as_view()),
]



