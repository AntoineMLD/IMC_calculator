# IMC_calculator

IMC Calculator

Cette application permet de calculer l'indice de masse corporelle (IMC) d'un utilisateur et de sauvegarder les résultats dans une base de données SQLite.
Description

L'IMC Calculator est une application de bureau développée en Python avec Tkinter pour l'interface graphique.

Elle permet à un utilisateur de saisir ses informations personnelles (nom, prénom, email, etc.) ainsi que son poids et sa taille. L'application calcule alors son IMC et l'enregistre dans une base de données SQLite, ainsi que l'historique des IMC précédents.

L'objectif est de fournir un outil simple pour suivre l'évolution de son IMC au fil du temps.
Installation

Les pré-requis sont :

    Python 3
    Les bibliothèques Tkinter, SQLAlchemy, sqlite3

Pour installer :

    Cloner le repository
    Exécuter bdd_init.sh pour initialiser la base de données
    Exécuter python schema.py pour créer les tables dans la BDD
    Exécuter python ui.py pour lancer l'interface graphique

Utilisation

L'interface graphique contient des champs pour saisir les informations de l'utilisateur, son poids et sa taille.

Une fois les valeurs renseignées, cliquer sur le bouton "Calculer" déclenche :

    Le calcul de l'IMC
    L'enregistrement dans la BDD via l'objet User et la table BMI
    La création d'un historique dans la table History



L'architecture utilise le modèle MVC avec :

    ui.py : programme principal avec l'interface Tkinter (vue)
    schema.py : définition des modèles SQLAlchemy (modèle)
    interface.py : fonctions pour interagir avec la BDD (contrôleur)

La base de données SQLite est créée avec bdd_init.sh et supprimée avec delete_bdd.sh.


Auteur
Antoine MOULARD
