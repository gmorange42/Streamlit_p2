#!/bin/bash

echo "Creation de l'environnement python"
python -m venv streamlit_env

echo "\nActivation environnement:"
source streamlit_env/Scripts/activate

echo "\nUpdate pip"
python.exe -m pip install --upgrade pip

echo "\nInstallation dependances requises"
pip install -r requirements.txt

