# Prérequis

`pyenv virtualenvs` liste les environnements virtuels
`pyenv virtualenv 3.7.2 my-virtual-env` création d'un environnement python 3.7.2
`pyenv activate my-virtual-env` active l'environnement virtuel

`python -m pip install -U pip --user` update pip
`pip install django` install flask

`pip install -r requirements.txt`

## Modèles

### Shell

`DataBase.objects.filter(codgeo='39058')`

`for el in DataBase.objects.all():`
`    print(el.codgeo)`

## Django REST Framework

### CRUDE

- Create
- Retrieve : ListAPIView / RetrieveAPIView
- Update
- Delete

### RETRIEVE

#### ListAPIView

#### RetrieveAPIView

- `lookup_field = 'nom_du_champ'`