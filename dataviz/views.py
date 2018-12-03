#Standard library imports

# Django imports
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

# third-party
from datetime import datetime
import pygal

# local Django
from dataviz.models import Statistiques

# page "accueil" avec la fonction render qui prend 3 arguments en paramètre : 
# la requête HTTP initiale
# le template home.html 
# un dictionnaire reprenant les variables qui seront accessibles dans le template

#
class SocioDemo(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
	data = (Statistiques.objects.values("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop")[0])
	return JsonResponse(data)

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		labels = ["1968", "1975", "1982", "1990", "1999", "2010", "2015"]
		filtre = Statistiques.objects.values_list("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop").filter(codgeo='39518')
		default_items = [el for el in filtre[0]]
		data = {
			"labels": labels,
			"default": default_items,
		}
		return Response(data)

def accueil(request):
	return HttpResponse("""
        <h1>ACCUEIL</h1>
        """)

def index2(request):
    return HttpResponse("""
        <h1>SOCIO DEMO</h1>
        """)

def index3(request):
    return HttpResponse("""
        <h1>ECO EMPLOI<h1>
        """)