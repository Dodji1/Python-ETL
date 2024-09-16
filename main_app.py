import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Fonction pour vérifier les identifiants de l'utilisateur
def check_credentials(username, password):
    # Ceci est une vérification simple pour la démonstration. Vous pouvez remplacer cela par une vérification plus sécurisée.
    return username == "admin" and password == "12345"

# Fonction pour la page de login
name = "admin"
mp = "12345"
def login_page():
    st.title("Page de Connexion")

    username = st.text_input("Nom d'utilisateur", name)
    password = st.text_input("Mot de passe", mp, type="password")
    
    if st.button("Se connecter"):
        if check_credentials(username, password):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")

# Fonction pour la page ETL et de monitoring
def etl_monitoring_page():
    st.title("Tableau de Bord ETL et Monitoring")
    
    # Téléchargement de fichier local
    uploaded_file = st.file_uploader("Choisir un fichier", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Aperçu du fichier téléchargé:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Erreur lors du chargement du fichier: {e}")

    # Web scraping
    st.subheader("Web Scraping")
    url = st.text_input("Entrer l'URL pour le scraping")
    if st.button("Scraper"):
        if url:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                st.write("Contenu de la page web:")
                st.code(soup.prettify()[:500])  # Affiche une partie du contenu pour éviter un trop long output
            except Exception as e:
                st.error(f"Erreur lors du scraping: {e}")

    # Appel à une API REST
    st.subheader("Appel à une API REST")
    api_url = st.text_input("Entrer l'URL de l'API")
    if st.button("Appeler l'API"):
        if api_url:
            try:
                response = requests.get(api_url)
                data = response.json()
                st.write("Réponse de l'API:")
                st.json(data)
            except Exception as e:
                st.error(f"Erreur lors de l'appel à l'API: {e}")

# Main application logic
def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    if not st.session_state['authenticated']:
        login_page()
    else:
        etl_monitoring_page()

if __name__ == "__main__":
    main()
