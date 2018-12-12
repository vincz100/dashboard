#Standard library imports

# Django imports
from django.contrib.auth import get_user_model, authenticate, login
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
from .forms import HomeForm, LoginForm

def home(request):
	return render(request, 'home.html', {})

class LoginView(TemplateView):
	template_name = "login.html"

	def get(self, request):
		form = LoginForm()
		return render(request, self.template_name, {"form": form})
	
	def post(self, request):
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # verif de données correctes avec la méthode authenticate(request, username=None, password=None). Renvoi soit un utilisateur authentifié, soit None
			if user is not None :
				login(request, user)
				return redirect('choice')
			else:
				error = True
		else:
			form: LoginForm()
		return render(request, self.template_name, locals())
		
class HomeView(TemplateView):
	template_name = "choice.html"

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {"form": form})
	
	def post(self, request):
		form = HomeForm(request.POST or None)
		if form.is_valid():
			text = form.cleaned_data['codgeo']
			args = {"form": form, "text": text}
			filtre = {"text": text}
			request.session["filtre"] = filtre
			return redirect('socio-demo')
		else:
			print('ERROR FORM INVALID')
		return render(request, self.template_name, args)

def board(request):
	return HttpResponse("""
		<h1>BOARD</h1>
		""")

class Population(View):

	def get(self, request, *args, **kwargs):
		filtre = request.session.get('filtre')
		filtre = filtre["text"]
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
		filtre = request.session.get('filtre')
		filtre = filtre["text"]
		stats = Statistiques.objects.get(codgeo=filtre)
		data = {
			"territory": [stats.libgeo],
			"labels": ["1968", "1975", "1982", "1990", "1999", "2010", "2015"],
			"default": [stats.d68_pop, stats.d75_pop, stats.d82_pop, stats.d90_pop, stats.d99_pop, stats.p10_pop, stats.p15_pop]
		}
		return Response(data)