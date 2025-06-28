#!/bin/sh

echo "Ouverture de streamlit_env"
source streamlit_env/Scripts/activate

echo "Lancement de l'app"
streamlit run Accueil.py
