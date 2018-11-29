from django.urls import path

from . import views
from dataviz.views import HomeView, get_data

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('api/data/', get_data, name='api-data'),
    path('accueil/', views.accueil, name='accueil'),
    path('socio_demo/', views.index2, name='index2'),
    path('eco_emploi/', views.index3, name='index3'),
]



