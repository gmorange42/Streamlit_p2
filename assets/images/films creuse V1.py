import streamlit as st
import pandas as pd
import pathlib

# Configurer votre application streamlit (toujour en premier sur streamlit)
st.set_page_config(
  
    layout="wide", initial_sidebar_state="collapsed"
 
)


# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load the external CSS
css_path = pathlib.Path("assets\style.css")
load_css(css_path)

st.markdown("<h1 >Creuse et Creusois au cinéma </h1>", unsafe_allow_html=True)

st.write(" ")

##### CLAUDE CHABROL #####
st.markdown("<h3 > Claude Chabrol, réalisateur</h3>", unsafe_allow_html=True)
st.markdown("<h3 > A vécu une partie de son enfance à Sardent </h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/myzAC2aVHhqLxzb7Bqo7xVtOloG.jpg") #use_container_width=True

st.markdown("<h3 >Ses films :</h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w150_and_h225_bestv2/An2gkXn5TATag9Adul2Zbq5Ndrv.jpg")
st.image("https://media.themoviedb.org/t/p/w150_and_h225_bestv2/gIBOAemklR8MVYP0Vn5RE0MYYWT.jpg")
st.image("https://media.themoviedb.org/t/p/w150_and_h225_bestv2/4QEL8tsDBZkBq54AzpTyFE4yY50.jpg")
st.image("https://media.themoviedb.org/t/p/w150_and_h225_bestv2/cBJtWAgDTCqxNJJOZjnRSh5Vxa5.jpg")

st.write(" ")

##### CLAUDE MILER #####
st.markdown("<h3 > Claude Miller, réalisateur</h3>", unsafe_allow_html=True)
st.markdown("<h3 > A vécu à Chavanat </h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w600_and_h900_bestv2/c9h4B4kFWgU4Jf2ciUzoDVD4IOU.jpg")

st.markdown("<h3 >Ses films :</h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/jtxhyGaYhurH6KsjvP1jV3dDypz.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/e9p8VdsAKXz1GoVXD36Lg5e3YKo.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/lKB8bOpJhTTxfiK5OWjilZeZ0Kc.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/8KcpHL8hjqBxZnMTMITGh8MNAhh.jpg")

##### Micheline Presle #####
st.markdown("<h3 > Micheline Presle, comédienne</h3>", unsafe_allow_html=True)
st.markdown("<h3 > A découvert la Creuse grâce à Nathalie Baye </h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w600_and_h900_bestv2/l3JEGPsntAwicRgZaNelmVoYGmg.jpg")

st.markdown("<h3 >Ses films :</h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/mZ5pUyr9bOPIl0PfkZenMGSr9iN.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/n5hHf0x8i62kbUycqHgkop7jUDy.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/kFxmjIcfsxDeiuna9SzPPtzwlZ4.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/faimmushRwen8519t2vBBAWjrUr.jpg")

##### Annie Duperey #####
st.markdown("<h3 > Annie Duperey, comédienne</h3>", unsafe_allow_html=True)
st.markdown("<h3 > Réside à Châtelus-Malvaleix </h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w600_and_h900_bestv2/2R4wfzsBmv3G43AKou6pS76iIA2.jpg")

st.markdown("<h3 >Ses films :</h3>", unsafe_allow_html=True)
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/rkFslveTXi5vIIGX0Icys8Hz8Zc.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/w1LO1SIrpA4GCjK3ysANr7F3eAN.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/yFWMa7JatOBYwbuDcokjVbTuYWK.jpg")
st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/eO8O5SwT1bQMHtW6kqEPteMVeiX.jpg")
