from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# page d'accueil "home" avec la fonction render qui prend 3 arguments en paramètre : 
# la requête HTTP initiale
# le template home.html 
# un dictionnaire reprenant les variables qui seront accessibles dans le templat
def home(request):
	return render(request, "templates/home.html", {"date": datetime.now()})

# page index avec la méthode HttpResponse(text) qui prend comme paramètre une chaîne de caractères et renvoie le HTML au navigateur. 
def index(request):
    return HttpResponse("""
        <h1>SOCIO DEMO</h1>
        """)

def index2(request):
    return HttpResponse("""
        <h1>ECO EMPLOI<h1>
        """)