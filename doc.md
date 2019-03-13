# Wiki

Imaginons une appli "communication / concertation / gestion de projet" à destination des acteurs territoriaux mais pas que. L'idée, un portail unique pour gérer son projet avec une gestion des scopes qui permet aux citoyens, politiques, techniciens, BE d'échanger, partager, travailler sur un même projet au sein d'une même appli avec :

- News : l'actualité du projet
- Agenda : les rdv / réunions / évènements
- Story : l'histoire du projet avec données et dataviz
- Cartes : pour visualiser les données territoriales liées au projet
- Concertation : formulaires, contribution, réseau social...
- Documents : une banque de documents pour télécharger / déposer des docs

Quel intérêt ? Quelles autres fonctionnalités ?

## Prérequis

`pyenv virtualenvs` liste les environnements virtuels
`pyenv virtualenv 3.7.2 my-virtual-env` création d'un environnement python 3.7.2
`pyenv activate my-virtual-env` active l'environnement virtuel

`python -m pip install -U pip --user` update pip
`pip install django` install flask

`pip install -r requirements.txt`

## Fonctionnalités

### News

Les news du projet (cf libe)

- Header = timeline avec les principaux évènements du projet
- Focus sur la dernière actualité avec une photo grand format (`last-update`)
- liste des actualités sous forme de vignette
- Focus 2 sur les 5 news les plus consultés

### Dashboard

###

## Modèles

## MCD

User

- uid
- name
- email
- login
- projects

## Définition des urls

`/` page d'accueil = présentation du produit, fonctionnalités...

- Bouton se connecter
- formulaire POST de demande d'infos (l'utilisateur envoie son nom + prénom + adresse mail)

`login/` page de connexion utilisateur

- formulaire POST de connexion (id + mdp)- lien "j'ai oublié mon mot de passe"

`recover/`

`logout/` bouton se déconnecter

- profile
  - `profile`

`front/<lib_projet>/` page sur laquelle on retrouve les apps de l'utilisateur (gestion du scope)

`front/<lib_projet>/<app>/`

- le home de chaque app donne accès aux différents panel (gestion du scope) :
  - `front/<lib_projet>/agenda/` : calendrier du projet (timeline, planning)
  - `front/<lib_projet>/news/` : dernieres actualités sous forme de caroussel
  - `front/<lib_projet>/dashboard/` : thématiques avec 1 ou 2 indicateurs clé
  - `front/<lib_projet>/project/` : cartes animées (story map)
  - `front/<lib_projet>/map/` : webmapping
  - `front/<lib_projet>/concertation/` : formulaire, contribution
  - `front/<lib_projet>/documents/` : banque de documents où chaque utilisateur peut télécharger et/ou déposer des docs

- admin
  - `admin/<lib_projet>/`

## Shell

`from dataviz.models import DataBase`
`DataBase.objects.filter(codgeo='39058')`
`DataBase.objects.filter(codgeo='39058').values('d68_pop', 'd75_pop')`
`DataBase.objects.filter(codgeo='39058').values_list('p15_pop','p10_pop')`

`for el in DataBase.objects.all():`
`print(el.codgeo)`

## News

### Nouvelle app

`python manage.py startapp news`

news/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py


### Modèle

`python manage.py createsuperuser`

`python manage.py migrate`

`python manage.py makemigrations news` En exécutant makemigrations, vous indiquez à Django que vous avez effectué des changements à vos modèles (dans ce cas, vous en avez créé) et que vous aimeriez que ces changements soient stockés sous forme de migration. Les migrations sont le moyen utilisé par Django pour stocker les modifications de vos modèles (et donc de votre schéma de base de données), ce ne sont que des fichiers sur le disque. Vous pouvez consultez la migration pour vos nouveaux modèles si vous le voulez ; il s’agit du fichier polls/migrations/0001_initial.py.

Par défaut, Django ajoute à chaque modèle le champ suivant :
`id = models.AutoField(primary_key=True)`

### Vues

Une vue est un exécutable acceptant une requête et renvoyant une réponse. Ce n’est pas forcément une simple fonction et Django fournit des exemples de classes qui peuvent être utilisées comme des vues. Celles-ci vous permettent de structurer vos vues et de réutiliser du code en exploitant l’héritage et les « mixins ».

Une vue basée sur une classe est déployée dans un motif d’URL en utilisant la méthode de classe as_view()

```
urlpatterns = [
    path('view/', MyView.as_view(size=42)),
]

```


## Django REST Framework

### CRUDE

- Create
- Retrieve : ListAPIView / RetrieveAPIView
- Update
- Delete

### RETRIEVE

Il s'agit de vue générique "Concrete View Classes". On importe les classes depuis `rest_framework_generics`.
On utilise ces vues lorsque l'on a pas besoin de customiser l'API.

#### ListAPIView

- read-only endpoints afin de représenter une collection de modèle

#### RetrieveAPIView

- read-only endpoints afin de représenter une seule collection de modèle
- `lookup_field = 'nom_du_champ'`