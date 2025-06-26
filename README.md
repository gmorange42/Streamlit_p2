
ce fichier readme contient une description des différent dossier et fichier du projet
# Rappel (installation environement virtuel)
python3 -m venv nom_env -> ceci crée un dossier mon_env dans votre projet , pour chaque projet faut penser à créer votre environement virtuel dans lequel on fera les installation des librairies(d'ailleur qu'il faut ignorer dans gitignore)


sur bash activer l'environnement virtuel
 source nom_env/Scripts/activate

# dossier .streamlit 

 Contient les fichiers de configuration :  ici le fichier config.toml permet de definir certain critere de style de la page : couleur police , couleur page ....

 # dossier assets
 Stocke les ressources statiques comme les images et fichiers CSS.

 # dossier data
 Regroupe les fichiers de données nécessaires à l'application

 # dossier pages

 Regroupe les fichiers de données nécessaires à l'application

 # app.py

 fichier principale pour lancer l'application streamlit

 # notebook_explore.ipynb 
 
 Un notebook pour explorer et tester les données ou modèles avant de les intégrer.

 # requirements

 Liste les dépendances nécessaires pour exécuter le projet
 (les librairies python)

 pour info pour créer un requirement de votre projet :

 pip list --not-required --format=freeze > requirements.txt

 pour installer toutes les librairies à partir du requirement:

 pip install -r requirements.txt

 # ressources

 faire du css sur streamlit
 https://youtu.be/jbJpAdGlKVY

 exemple de github pour projet streamlit
 https://github.com/Sven-Bo/streamit-css-styling-demo
# projet2
# Streamlit_p2
# Streamlit_p2
