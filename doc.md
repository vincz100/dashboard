# Prérequis

`pyenv virtualenvs` liste les environnements virtuels
`pyenv virtualenv 3.7.2 my-virtual-env` création d'un environnement python 3.7.2
`pyenv activate my-virtual-env` active l'environnement virtuel

`python -m pip install -U pip --user` update pip
`pip install django` install flask

`pip install -r requirements.txt`

## Modèles

### Shell
`from dataviz.models import DataBase`
`DataBase.objects.filter(codgeo='39058')`
`DataBase.objects.filter(codgeo='39058').values('d68_pop', 'd75_pop')`
`DataBase.objects.filter(codgeo='39058').values_list('p15_pop','p10_pop')`

`for el in DataBase.objects.all():`
`    print(el.codgeo)`

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

