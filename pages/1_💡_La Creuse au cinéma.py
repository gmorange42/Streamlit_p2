import streamlit as st
import pandas as pd
import pathlib

# Configurer votre application streamlit (toujour en premier sur streamlit)
st.set_page_config(
  
    layout="wide", initial_sidebar_state="collapsed")

# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load the external CSS
css_path = pathlib.Path("assets/style.css")
load_css(css_path)



st.markdown("<h1 style='text-align: center'> Découvrez les personnalités du cinéma qui ont marqué La Creuse </h1>", unsafe_allow_html=True)
st.markdown("<h3> Souvent perçue comme un havre de paix rural, La Creuse a pourtant tissé des liens profonds avec plusieurs grandes figures du cinéma français. Loin des plateaux parisiens, ce département discret a servi de décor, de refuge ou d'inspiration pour des artistes majeurs. </h3>", unsafe_allow_html=True)

cols_photos = st.columns(4)
with cols_photos[0]:
    st.image("https://lespierresjaumatres.fr/wp-content/uploads/2021/06/visiter-la-Creuse-lieux-incontournables-le-chalet-des-Pierres-Jaumatres-Aubusson.jpg")
with cols_photos[1]:
    st.image("https://www.aquitaineonline.com/images/stories/Limousin/Creuse_23a.jpg")
with cols_photos[2]:
    st.image("https://passion-aquitaine.ouest-france.fr/wp-content/uploads/2025/04/aubusson-creuse-village.jpg")
with cols_photos[3]:
    st.image("https://passionlimousin.fr/wp-content/uploads/2023/02/creuse-1024x576-1.jpg")

st.write("\n")
st.write("\n")
st.write("\n")

# Boutons qui permet d'afficher les descriptions des personnalités
st.markdown("<h3> Sélectionnez une personnalité si vous voulez en savoir en plus sur celle-ci : </h3>", unsafe_allow_html=True)
claude_c    = st.checkbox("Claude Chabrol, réalisateur")
claude_m    = st.checkbox("Claude Miller, réalisateur, scénariste et producteur ")
anny_d      = st.checkbox("Anny Duperey, actrice")
micheline_p = st.checkbox("Micheline Presle, actrice")

# Création de 3 colonnes 
cols_page = st.columns([10,1,10])

##### CLAUDE CHABROL #####
if claude_c :
    with cols_page[0]:
        st.markdown("<h2 style='text-align: center' > Claude Chabrol </h2>", unsafe_allow_html=True)
        st.image("https://fr.web.img3.acsta.net/c_310_420/pictures/19/02/19/15/43/1517198.jpg", use_container_width=True)

    with cols_page[2]:
        st.markdown("<h2 > 💝Son lien avec La Creuse </h2>", unsafe_allow_html=True)
        st.markdown(""" <h5 > Célèbre réalisateur français, son attachement à la Creuse, et plus spécifiquement au village de Sardent, où il passa de nombreux étés et une partie de son enfance, est bien connu. 
                    Cet ancrage rural fut même le décor de son tout premier long-métrage, Le Beau Serge (1958), considéré comme le film fondateur de la Nouvelle Vague. </h5>""", 
                    unsafe_allow_html=True)
        st.image("https://www.sardent23.fr/userfile/img-photos/xl/1633697257-place--balustrade-23.JPG")
        
        st.markdown("<h2 > 💡Anecdote creusoise  </h2>", unsafe_allow_html=True)      
        st.markdown("""<h5 > Lorsqu'il préparait le tournage du "Beau Serge", il avait besoin de figuration locale. 
                        Il se rendit dans le village de Sardent et, avec son sens de l'humour habituel, expliqua aux habitants qu'il voulait faire un film avec eux. 
                        La scène se passait dans l'église du village. Cependant, les habitants, peu habitués aux méthodes de cinéma, avaient du mal à rester silencieux pendant les prises. 
                        Sans s'énerver, il trouva une solution simple et amusante. Il fit promettre à toute la figuration qu'après chaque scène réussie, il y aurait une grande tablée avec du pâté de pommes de terre et du vin. 
                        Le résultat fut immédiat : les prises furent parfaites, et les habitants de Sardent devinrent des acteurs appliqués.</h5>""", 
                        unsafe_allow_html=True)
        sub_cols =st.columns(3)
        with sub_cols[1]:
            st.image("https://planete-vintage.com/cdn/shop/files/le-beau-serge-affiche_3_540x.webp?v=1707915358", use_container_width=True)

st.write("\n")
         
##### CLAUDE MILLER #####
if claude_m :
    with cols_page[0]:
        st.markdown("<h2 style='text-align: center' > Claude Miller </h2>", unsafe_allow_html=True)
        st.image("https://medias.unifrance.org/medias/198/169/43462/format_page/claude-miller.jpg", use_container_width=True)

    with cols_page[2]:
        st.markdown("<h2 > 💝Son lien avec La Creuse </h2>", unsafe_allow_html=True)
        st.markdown(""" <h5 > 
                    Claude Miller (1942-2012) fut un réalisateur, scénariste et producteur français, célébré pour son cinéma sensible explorant les tourments de l'enfance, de l'adolescence et les mystères des relations humaines.
                    C'est avec le film "Un secret" qui'il a réalisé en 2007 qu'il a tissé un lien particulier avec la Creuse.
                    </h5>""", 
                    unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/%C3%89glise_Saint-Jean-Baptiste_de_Chavanat_%281%29.jpg/1920px-%C3%89glise_Saint-Jean-Baptiste_de_Chavanat_%281%29.jpg")
        
        st.markdown("<h2 > 💡Anecdote creusoise  </h2>", unsafe_allow_html=True)      
        st.markdown("""<h5 > 
                    Claude Miller a choisi de tourner des scènes clés directement dans la commune de Chavanat, plus précisément au lieu-dit "Le Monteillard". 
                    Ce choix n'était pas anodin : il témoignait d'une recherche d'authenticité et d'une affinité avec les paysages de la Creuse.
                    Mais le lien ne s'arrête pas là. L'épouse de Claude Miller, Annie Miller, a fortement contribué à ancrer la présence des Miller dans la région en co-fondant l'association Lavaud-Soubranne. 
                    Cette association est active dans l'organisation d'ateliers d'écriture de scénarios et du festival "Ciné des villes ciné des champs" à Bourganeuf, toujours en Creuse. 
                    D'ailleurs, le cinéma de Bourganeuf porte désormais le nom de "Cinéma Claude Miller", un hommage durable à ce réalisateur qui, même s'il n'y est pas né, a trouvé en Creuse un lieu d'expression artistique et un point d'attache familial. 
                    L'amie du couple, Nathalie Baye, est également souvent créditée pour les avoir introduits à la beauté de cette région.
                    </h5>""", 
                    unsafe_allow_html=True)
        sub_cols =st.columns(3)
        with sub_cols[1]:
            st.image("https://media.themoviedb.org/t/p/w300_and_h450_bestv2/8KcpHL8hjqBxZnMTMITGh8MNAhh.jpg", use_container_width=True)

st.write("\n")

##### Anny Duperey #####
if anny_d:
    with cols_page[0]:
        st.markdown("<h2 style='text-align: center' > Anny Duperey </h2>", unsafe_allow_html=True)
        st.image("https://www.theatreonline.com/BDDPhoto/Medias/artiste/29038/1_affiche.jpg", use_container_width=True)

    with cols_page[2]:
        st.markdown("<h2 > 💝Son lien avec La Creuse </h2>", unsafe_allow_html=True)
        st.markdown(""" <h5 > 
                    Anny Duperey est une actrice française emblématique, également écrivaine et photographe, reconnue pour sa longue et riche carrière au cinéma, à la télévision et au théâtre.
                    Elle réside dans un village creusois, Châtelus-Malvaleix, depuis plus de 40 ans.</h5>""", 
                    unsafe_allow_html=True)
        st.image("https://api.cloudly.space/resize/clip/1900/1080/75/aHR0cHM6Ly9jZHQ0MC5tZWRpYS50b3VyaW5zb2Z0LmV1L3VwbG9hZC9Ecm9uZXBsYW5kZWF1Um91c3NpbGxlQ2hhdGVsdXNtYWx2YWxlaXgyMy0tQ3JldXNlVG91cmlzbWUtMy0uanBn/image.jpg")
        
        st.markdown("<h2 > 💡Anecdote creusoise  </h2>", unsafe_allow_html=True)      
        st.markdown("""<h5 >C'est en Creuse qu'elle a trouvé cet havre de paix.
                    Loin des paillettes, elle a choisi d'y acquérir une propriété où elle se ressource profondément. 
                    Elle y mène une vie discrète, loin des obligations médiatiques. 
                    On la dit très attachée à son jardin, à la lecture, et à la contemplation de la nature creusoise.</h5>""", 
                    unsafe_allow_html=True)
       
        st.image("https://www.lamontagne.fr/photoSRC/Gw--/annie-duperey-chez-elle-a-chatelus-malvaleix_6412894.jpeg", use_container_width=True)

st.write("\n")

##### Micheline Presle #####
if micheline_p :
    with cols_page[0]:
        st.markdown("<h2 style='text-align: center' > Micheline Presle </h2>", unsafe_allow_html=True)
        st.image("https://fr.web.img6.acsta.net/c_310_420/pictures/17/10/19/14/02/0161388.jpg", use_container_width=True)

    with cols_page[2]:
        st.markdown("<h2 > 💝Son lien avec La Creuse </h2>", unsafe_allow_html=True)
        st.markdown(""" <h5 > Actrice majeure des années 1940, Micheline Presle (1922-2024) fut une icône du cinéma français, traversant les époques avec élégance et mystère.
                    Elle a maintenu un lien particulier avec La Creuse. En effet, elle a vécu pendant quelques années à La Nouaille, un joli petit village de 290 habitants dans ce département.</h5>""", 
                    unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/La_Nouaille_-_Mairie_et_Monument_aux_Morts.JPG/1200px-La_Nouaille_-_Mairie_et_Monument_aux_Morts.JPG")
        
        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.markdown("<h2 > 💡Anecdote creusoise  </h2>", unsafe_allow_html=True)      
        st.markdown("""<h5 > Elle cherchait un havre de paix. C'est donc son amie actrice Nathalie Baye qui, dans les années 1980, l'aurait initiée et convaincue de la beauté et de la tranquillité de ce département rural. 
                    Séduite par le calme et la nature préservée, Micheline Presle a fini par acquérir et vivre pendant plusieurs années dans une petite maison isolée, au sein d'un village très modeste de seulement 290 habitants dans la Creuse. 
                    Elle y menait une vie simple, loin du tumulte parisien et des fastes de sa carrière cinématographique.</h5>""", 
                        unsafe_allow_html=True)
        sub_cols =st.columns(3)

        




