from django.urls import path

from . import views
from dataviz.views import Population, get_data, ChartData

urlpatterns = [
    path('', views.accueil, name='index'),
    path('socio_demo/', Population.as_view(), name='socio-demo'),
    path('eco_emploi/', views.index3, name='index3'),
    path('api/data/', get_data, name='api-data'),
    path('socio_demo/api/chart/data/', ChartData.as_view()),
]



