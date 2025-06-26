import streamlit as st  # pip install streamlit

st.set_page_config(page_title='Contact', page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)

st.header(":mailbox: Contactez-nous")


contact_form = """
<form action="https://formsubmit.co/cassiopea.wild@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Votre nom" required>
     <input type="email" name="email" placeholder="Votre email" required>
     <textarea name="message" placeholder="Votre message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("assets/style.css")