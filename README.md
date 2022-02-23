
# API de Gutenberg Project

Ce projet est le back-end d'une application web de moteur de recherche, basé sur [Gutenberg.org](https://gutenberg.org). Il permet notamment l'indexation et une recherche plus rapide sur quelques livres tirés de Gutenberg.

C'est un projet d'étudiant de Bac +5, fait au CFA INSTA en Février 2022.
## Auteurs

- [@Mar-Nb](https://github.com/Mar-Nb)
- [@Kuraihani](https://github.com/Kuraihani)
- [@Darkspace21](https://github.com/Darkspace21)

## Technologies utilisées

Pour ce projet, plusieurs technologies différentes sont utilisées :

* Framework Python **Django**
* Bibliothèques `json`, `requests`, `rest_framework` de Python (entre autres)

## Leçon(s) tirée(s)

La mise en place de ce back-end Django nous a permis de toucher de nouveau cette technologie découverte lors d'un précédent projet de cours. Cela nous a permis de voir l'utilisation de fichiers statiques, par exemple, pour pouvoir exploiter les fichiers JSON qui servent pour le moteur de recherche.

Nous avons toutefois été confrontés à quelques difficultés :

* Configuration des fichiers statiques
* *Parsing* des fichiers JSON

Une recherche sur **StackOverflow** et de multiples `print()` ont cependant permis de surmonter ces difficultés. Pour le parsing des fichiers, il a aussi été nécessaire de remplacer ou d'effacer les caractères qui empêchaient un parsing correct.

## Lancer le projet

Cloner le projet :

```bash
  git clone https://github.com/Mar-Nb/gutenberg-project-api.git
```

Aller dans le dossier du projet :

```bash
  cd gutenberg-project-api
```

Installer les dépendences (vous pouvez aussi les installer dans un environnement virtuel) :

```bash
  pip install django djangorestframework requests
```

Lancer le serveur :

```bash
  python manage.py runserver
```

Par défaut, le serveur écoute à l'adresse http://localhost:8000.

## API

#### Get all items

```http
  GET /myApi/livresAccueil
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `page` | `int` | **Optional**. La page courante |
| `isForward` | `boolean` | **Optional**. Le fait d'avancer vers la page suivante |
| `oldMax` | `int` | **Optional**. Ancien nombre max. de livres à afficher |


## En lien avec le projet

D'autres éléments en lien avec ce projet :

* [Front-End du projet](https://github.com/Kuraihani/GutenbergProject)
* [Rapport sur le développement de l'app](https://docs.google.com/document/d/1MXduRu2FFVqrqvTKN77Ns2Z7KbDmHeEulD1jMt_Qm0M/edit?usp=sharing)
* [Présentation du projet](https://docs.google.com/presentation/d/1WjbyExNHYzi3xzZsGLBNqcRQeA45QLeMRCVBYQMbeaQ/edit?usp=sharing)
