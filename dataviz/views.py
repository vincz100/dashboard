#Standard library imports

# Django imports
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

# third-party
from datetime import datetime
import pygal

# local Django
from .models import Statistiques
from .forms import HomeForm

filtre = '39192'

class HomeView(TemplateView):
	template_name = "accueil.html"

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {"form": form})
	
	def post(self, request):
		form = HomeForm(request.POST or None)
		if form.is_valid():
			text = form.cleaned_data['codgeo']
		else:
			print('ERROR FORM INVALID')

		args = {"form": form, "text": text}
		print(text)
		return render(request, self.template_name, args)

class Population(View):
	
	# filtre = get.text
	def get(self, request, *args, **kwargs):

		# codgeo = request.session['codgeo']
		stats = Statistiques.objects.get(codgeo=filtre)
		data = {
			"libgeo": stats.libgeo,
			"codgeo" : stats.codgeo
		}
		return render(request, 'charts.html', data)

def get_data(request, *args, **kwargs):
	data = (Statistiques.objects.values("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop")[0])
	return JsonResponse(data)

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		codgeo = request.session.get('codgeo')
		stats = Statistiques.objects.get(codgeo=filtre)
		data = {
			"territory": [stats.libgeo],
			"labels": ["1968", "1975", "1982", "1990", "1999", "2010", "2015"],
			"default": [stats.d68_pop, stats.d75_pop, stats.d82_pop, stats.d90_pop, stats.d99_pop, stats.p10_pop, stats.p15_pop]
		}
		return Response(data)

def index2(request):
    return HttpResponse("""
        <h1>SOCIO DEMO</h1>
        """)

def index3(request, text):
    return HttpResponse("""
        <h1>ECO EMPLOI<h1>
        """)