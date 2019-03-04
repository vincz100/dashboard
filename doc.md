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

`/` page home = présentation du produit, fonctionnalités...

- Bouton se connecter
- formulaire POST de demande d'infos (l'utilisateur envoie son nom + prénom + adresse mail)

`login/`
`recover/`

- formulaire POST de connexion (id + mdp)
- lien "j'ai oublié mon mot de passe"

`logout/`

- bouton se déconnecter

`home/`

- page sur laquelle on retrouve les apps de l'utilisateur (gestion du scope) :

`home/<app>/`

- le home de chaque app donne accès aux différents panel (gestion du scope) :
  - `home/agenda/` : calendrier du projet (timeline, planning)
  - `home/news/` : dernieres actualités sous forme de caroussel
  - `home/dashboard/` : thématiques avec 1 ou 2 indicateurs clé
  - `home/project/` : cartes animées (story map)
  - `home/map/` : webmapping
  - `home/concertation/` : formulaire, contribution
  - `home/documents/` : banque de documents où chaque utilisateur peut télécharger et/ou déposer des docs

### Shell

`from dataviz.models import DataBase`
`DataBase.objects.filter(codgeo='39058')`
`DataBase.objects.filter(codgeo='39058').values('d68_pop', 'd75_pop')`
`DataBase.objects.filter(codgeo='39058').values_list('p15_pop','p10_pop')`

`for el in DataBase.objects.all():`
`print(el.codgeo)`

## Nouvelle app



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

