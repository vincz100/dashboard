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
from .models import DataBase
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
		
class TerritoryChoice(TemplateView):
	template_name = "choice.html"

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {"form": form})
	
	def post(self, request, userinput=None):
		form = HomeForm(request.POST or None)
		if form.is_valid():
			userinput = form.cleaned_data['codgeo']
			args = {"form": form, "userinput": userinput}
			filtre = {"userinput": userinput}
			request.session["filtre"] = filtre
			return redirect('socio-demo', userinput)
		else:
			print('ERROR FORM INVALID')
		return render(request, self.template_name, args)

def board(request):
	return HttpResponse("""
		<h1>BOARD</h1>
		""")

class UserChoice(View):

	def get(self, request, *args, **kwargs):
		filtre = request.session.get('filtre')
		filtre = filtre["userinput"]
		stats = DataBase.objects.get(codgeo=filtre)
		data = {
			"libgeo": stats.libgeo,
			"codgeo" : stats.codgeo
		}
		return render(request, 'charts.html', data)

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		filtre = request.session.get('filtre')
		filtre = filtre["userinput"]
		stats = DataBase.objects.get(codgeo=filtre)
		data = {
			"territory": [stats.libgeo],
			"labels": ["1968", "1975", "1982", "1990", "1999", "2010", "2015"],
			"default": [stats.d68_pop, stats.d75_pop, stats.d82_pop, stats.d90_pop, stats.d99_pop, stats.p10_pop, stats.p15_pop],
			"evolpopan": [stats.txevopopan_6875, stats.txevopopan_7582, stats.txevopopan_8290, stats.txevopopan_9099, stats.txevopopan_9910, stats.txevopopan_1015],
			"compo_menages":[stats.c10_txmenpseul, stats.c10_txmensfam, stats.c10_txmencoupsenf, stats.c10_txmencoupaenf, stats.c10_txmenfammono],
			"soldmig":[stats.txevoansoldmig_6875, stats.txevoansoldmig_7582, stats.txevoansoldmig_8290, stats.txevoansoldmig_9099, stats.txevoansoldmig_9910, stats.txevoansoldmig_1015],
			"soldnat":[stats.txevoansoldnat_6875, stats.txevoansoldnat_7582, stats.txevoansoldnat_8290, stats.txevoansoldnat_9099, stats.txevoansoldnat_9910, stats.txevoansoldnat_1015],
		}
		return Response(data)