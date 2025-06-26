import streamlit as st
import pandas as pd

#Configuration de la page

st.set_page_config(page_title='Cine', page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)

# Define columns
col_header = st.columns([3,8,3])

# Set title in the first column
with col_header[1]:

    # Titre principal de l'application (affiché en haut de la page)
    st.title("CINEMA EDEN - LA SOUTERRAINE")
    # image
    st.image("https://www.ville-lasouterraine.fr/app/uploads/2022/04/eden-1024x768.jpg") 

col_infos = st.columns([1,3,1,3,1])

with col_infos[1]:
    # Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
    st.subheader("Contact")

    # Affiche une ligne de texte simple (sans mise en forme particulière)
    st.text("Place Saint-Jacques 23300 La Souterraine")
    st.text("telphone : 0555895175")

    st.subheader("Horaires")
    st.text("En période scolaire")
    st.text("Lundi : Fermé ")
    st.text("Mardi ,  Jeudi ,  Vendredi :  18h00,  20h30 ")
    st.text("Mercredi , Samedi : 15h00, 18h00, 20h30 ")
    st.text("Dimanche : 15h00 , 17h30,  20h30")
    st.text("Pendant les vacances scolaires :")
    st.text("Tous les jours (sauf lundi): 15h00, 18h00, 20h30 ")

with col_infos[3]:
    st.subheader("Tarifs")
    st.text("Plein : 7,00 €")
    st.text("Réduit (De 14 à 20 ans, étudiants, chômeurs, handicapés, 65 ans et plus) : 5,50 € ")
    st.text("Mercredi (pour tous) : 5,50 € ")
    st.text("Super réduit (moins de 14 ans) : 4 € ")
    st.text("Supplément film 3D : 2 € ")
    st.text("Comédie française (dans le cadre scolaire): 4 € ")
    st.text("Comédie française (adultes): 12 € ")
    st.text("CE, Groupement du personnel (vendu par multiple de 10): 6,20 € ")
    st.text("Carte d’abonnement : 2 € ")
    st.text("Remplacement carte d’abonnement: 2 € ")
    st.text("Abonnement 5 séances (vendu par multiple de 5): 31 € ")
    st.text("Accompagnateur scolaire, IME, EHPAD: gratuit ")