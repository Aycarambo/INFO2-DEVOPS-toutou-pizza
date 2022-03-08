**Godard Nicolas,**  
**Terral Baptiste**  
**Stanislas Lucas**  
**Lalida Lucas**  

<br>

# <center> **DEVOPS4 - Compte-rendu de groupe**

##  **TD 1**

<br>

## **Routes**

Les routes REST sont placées dans différents fichiers.
Dans le fichier "toutou-pizza/urls.py", on retrouve les routes principales de l'API (admin/, api-auth/ et api/v1/).

Pour chacun de ces paternes, des sous-routes existent.
Dans le fichier "api/urls.py" par exemple, nous avons les sous-routes de la route api/v1/ :

```
pizzas
pizza/<str:name>

restaurants
restaurant/<str:name>

orders/<int:pk>
```

A ces routes, un ensemble d'attributs sont précisés via le fichier "share/data.json".

Par exemple, sur cet extrait de data.json, on va ajouter une page "restaurant/Reine" en renseignant son prix et ses ingrédients :

```
{
    "model": "restaurant.pizza",
    "pk": 1,
    "fields": {
      "name": "Reine",
      "price": 9,
      "ingredients": [
        1,
        2,
        3,
        4,
        5,
        6
      ]
    }
  },
```

<br>

## **Requirements.txt**

Sur un Gitlab tutoriel du framework REST, nous avons trouvé le fichier requirements.txt nécessaire à l'installation du serveur Django.

Dans ce fichier, nous avons une liste de librairies à installer et leurs versions (Django 3.1.8, djangorestframework 3.11.2, ...).

<br>

## **.gitignore**

Sur gitignore.io, nous avons généré le fichier .gitignore du projet en ignorant VSCode, Python et Django.

Grâce à ça, les prochains push ignoreront les fichier créés automatiquement par ces différentes applications.

<br>

## **Résumé TD1** 

Nous avons pu comprendre l'architecture REST de façon globale. Nous nous sommes connecté au système et avons pu naviguer au travers des différentes pages du projet toutoupizza.

```
Script de la reconnexion au système :

-> On se place dans le dossier
cd toutoupizza

-> On active py3venv
source py3venv/bin/activate

// On teste la connexion
Tester : which python3

// On lance le serveur
python3 manage.py runserver
```

<br>

---

<br>

## **TD2**

<br>

## **Tests**

Afin d'obtenir une couverture tests convenable, nous avons imaginés plusieurs tests à faire :

```
Vérification de la conformité de plusieurs objets dans la base de donnée à leur création
  - Test si un ingrédient allergène est bien allergène
  - Test du prix d'une pizza
  - Test du nombre d'ingrédient sur une pizza
  - Test de la conformité d'une commande
  - Test du nom et de l'adresse d'un restaurant
  - Test de la conformité d'une adresse

Vérification de la conformité des routes
  - Test si l'url api-auth/ renvoie un code HTTP 200 de succès
  - Test si l'url admin/ renvoie un code HTTP 200 de succès
  - Test si l'url api/v1/ renvoie un code HTTP 200 de succès

Test sur l'API
  - Test si la création d'un objet s'est bien réalisée
  - Test si la suppression d'un objet s'est bien réalisée
```

<br>

## **Métrique**

Avec tout ces tests, nous avons eu une coverage moyenne sur l'ensemble des fichiers d'environ 54%. Ce pourcentage semble cohérent avec le peu de tests que nous avons écrits.
En entreprise, ce serait bien insuffisant. Si nous avions plus de temps, il faudrait doubler ce nombre de tests.

<br>

---

<br>

## **TD3**

<br>

## **Les Patchs**

Un patch (fichier .patch) est un fichier contenant du code formaté. Il permet de modifier du code existant en ajoutant ou modifiant des fonctionnalités. 
De plus, un patch va permettre d'ajouter le code en question dans la copie d'un fichier déjà existant plutôt que de directement remplacer ce fichier par un nouveau.

<br> 

<br> 

## **Nous nous sommes arrêtés ici**
