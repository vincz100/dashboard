from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home, name='home'),
    path('socio_demo', views.index, name='index'),
    path('eco_emploi', views.index2, name='index2'),
]



