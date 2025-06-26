import streamlit as st
import pandas as pd
import pathlib
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    layout="wide",                # Utilise toute la largeur de l'écran
    initial_sidebar_state="collapsed"  # La sidebar est réduite par défaut
)

def load_css(file_path): #je charge et applique le fichier CSS personnalisé présent dans assets
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("assets\style.css")
load_css(css_path)

#je mets mon image, titre et texte, avec des saust de ligne ou lignes vides

st.image("assets/images/eden +.png") 
st.markdown("<h1 >Rencontrez...<br> ...vos films préférés!</h1>", unsafe_allow_html=True)

st.text("")

st.markdown("<h3 >Explorez notre base et vivez de nouvelles expériences cinématographiques qui vous correspondent.</h3>", unsafe_allow_html=True)
st.markdown("<h3 >Vous avez vos préférences ? Nous vous recommandons une sélection de films adaptés à celles-ci.</h3>", unsafe_allow_html=True)
st.markdown("<h3 >Explorez notre base et vivez de nouvelles expériences cinématographiques qui vous correspondent.</h3>", unsafe_allow_html=True)

st.title("")

#je crée trois colones pour y mettre mes trois boutons 
# sur lesquels je vais appliquer des style différents présents dans style.css
# et chaque bouton renvoie vers une page différente du site

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns(2)
# Carte 1
with col1:
    if st.button("Trouvez les films qui vous correspondent", icon="🎞️", type= "secondary"):
        test =   st.switch_page( "pages/1_🎞️_Nos recommandations.py")
    st.text("")
    if st.button("Découvrez notre cinéma Eden", icon="🎥",type= "secondary"):
        st.switch_page("pages/4_🎥_Notre cinéma.py")



# Carte 2
with col2:
    if st.button("Bonus : La Creuse au cinéma", icon="💡",type= "secondary"):
        test =   st.switch_page( "pages\\2_💡_Films en Creuse.py") #\\: si je mets un \ ave cun caractère derrière, ça veut dire qqch de spécifique. Av ecun second \, j'annule cette demande spécifique
    st.text("")
    if st.button("Contactez-nous", icon="✍️", type= "secondary"):
        st.switch_page("pages/5_✍️_Contacts.py")

# Carte 3
#with col3:
#    if st.button("Explorez notre fonds cinématographique", icon="🎬", type= "secondary"):
#        test =   st.switch_page( "pages/3_🎬_Fonds cinématographique.py") #ou sinon, je peux juste changer mon \ en /"""

st.title("")

#if st.button("Nous contacter"):
 #   st.switch_page("pages/4_✍️_Contacts.py")


#if st.button("Découvrir notre cinéma"):
 #   st.switch_page("pages/5_❔_Notre cinéma.py")
#st.markdown("[Découvrir notre cinéma](cinema)", unsafe_allow_html=True)