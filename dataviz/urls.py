from django.urls import path

from . import views
from dataviz.views import SocioDemo, get_data, ChartData

urlpatterns = [
    path('', views.accueil, name='index'),

    path('api/data/', get_data, name='api-data'),

    path('socio_demo/', SocioDemo.as_view(), name='socio-demo'),
    path('socio_demo/api/chart/data/', ChartData.as_view()),

    path('eco_emploi/', views.index3, name='index3'),
]



