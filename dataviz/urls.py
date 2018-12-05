from django.urls import path
from django.contrib import admin
from . import views
from dataviz.views import Population, get_data, ChartData

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.accueil, name='index'),
    path('socio_demo/', Population.as_view(), name='socio-demo'),
    path('eco_emploi/', views.index3, name='index3'),
    path('api/data/', get_data, name='api-data'),
    path('socio_demo/api/chart/data/', ChartData.as_view()),
]



