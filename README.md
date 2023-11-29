# PronotePyEasy

*Une façon d'accèder à Pronote simplement pour les débutants*



## Introduction

**PronotePyEasy** est un modules python additionnel à [PronotePy](https://github.com/bain3/pronotepy)

Il néccesite donc exactement les mêmes modules pour fonctionner.

> [!IMPORTANT] 
> Si vous avez un bon niveau en python (niveau moyen ou plus), je vous encourage a aller utiliser *PronotePy* directement.
> Il un peu difficile à utiliser pour les tous nouveau utilisateur de python de par sont utilisation d'objet.
> Cependant, avec son [Wiki](https://pronotepy.readthedocs.io/en/stable/), PronotePy est facile d'utilisation pour les personnes ayant les notions fondamental en POO python. 
> De plus si vous envisagez d'apprendre la POO *(Programmation Orienté Objet)* en python, PronotePy est un bon moyen de commencer (J'ai appris grâce à cela) 

## Fonctionnement

### Connexion au compte Pronote

```python
import pronotepy
import PronotePyEasy

etab = "https://demo.index-education.net/pronote/eleve.html"
client = pronotepy.Client(etab,
                          username='demonstration',
                          password='pronotevs')
```

Cette étape est la même que sur PronotePy, en cas de problème à cette étape, ou pour plus d'option :
s'en référer au module pronotepy

### Initialisation de PronotePyEasy

```python
eleve = PronotePyEasy.Student(client)
```

`eleve` devient dès lors l'objet afin d'appeler les fontions du module (voir suite pour comprendre)

## Utilisation

### Obtenir les devoirs

```python
print(eleve.next_homework())
```

Pour obtenir le prochain devoir de l'èlève.
Renvoie une list avec :
- Nom de la matière (str)
- Le contenue du devoir (str)
- La date pour laquel il faut rendre le devoir (date)
- Si le devoir a été fait (bool)

```python
print(eleve.homework())  # Renvoie tous les prochains devoir
print(eleve.homework(3))  # Renvoie les 3 prochains devoir (dans la limites des prochains devoirs)
```

Idem que `next_homework()` mais renvoie tous les devoirs, ou le nombre données en argument *optionnel*.
Renvoie sous la même forme.

### Obtenir la moyenne

```python
print(eleve.average())
```

Renvoie la moyenne général sous forme d'un float

### Obtenir les infos et sondages

```python
print(eleve.informations_polls(83))  # Renvoie les 83 dernières informations/sondages (dans la limites des infos etc...)
```

Renvoie la listes des informations et sondages publiés, ou le nombre données en argument *optionnel*.
Renvoie une list contenant une list par infos/sondages sous forme:
`[Titre (str)/ Auteur (str)/ Contenue(str)/ Date(date)/lu (bool)]`

### Obtenir les absences

```python
print(eleve.absences())
```

Renvoie la listes des absence enregistré, ou le nombre données en argument *optionnel*.
Renvoie une list contenant une list par absence sous forme:
`[Nombre d'heure (str)/ Raison (list[str])/ Justifié(bool)]`

### Obtenir les absences

```python
print(eleve.grades())
```

Renvoie la listes des notes enregistré, ou le nombre données en argument *optionnel*.
Renvoie une list contenant une list par note sous forme:
`[Note (str)/ Sur combien est la note (str)/ Matière (str)]`

> [!WARNING]
> En cas d'abus du modules vous risquez les mêmes choses que précise le module PronotePy

## License

Aucunes car je sais pas comment ça fonctionne (yet)