# P13 - Vers l'infinie et l'au-delà !

**Stars news** est un blog développé dans le cadre de mon projet de fin de parcours sur OpenClassrooms.

## **Installation**
Après avoir cloné le repo, creez un nouvel environnement virtuel ( de préférence dans le dossier du projet ):

1°) **virtualenv env -p python3**

Puis, activez le:

2°) **source env/bin/activate**

Ensuite, installez avec pip les dépendances de l'application:

3°) **pip install -r requirements.txt**

Une fois ceci fait, créer vous une nouvelle base de données (vers_linfinie) puis un nouvel utilisateur possédant tous les droits sur la base de données.
Configurez la partie "DATABASES" dans le fichier "settings.py" qui se situe dans le dossier "vers_linfinie". Faites en sorte que les informations de connexions correspondent.

Définissez également votre variable "STATIC_ROOT" puis faites un collectstatic de cette manière:

4°) **python3 manage.py collectstatic**

Faites les migrations:

5°) **python3 manage.py migrate**

Pour conclure, créer un super utilisateur:

6°) **python3 manage.py createsuperuser**

L'application peut enfin être lancer de cette façon:

7°) **python3 manage.py runserver**



