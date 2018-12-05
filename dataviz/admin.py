from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Statistiques, MushroomSpot
# ne pas oublier d'importer le modèle !

admin.site.register(MushroomSpot, LeafletGeoAdmin)