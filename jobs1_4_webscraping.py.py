import requests                        # bibliothèque pour communiquer avec la page web.
from bs4 import BeautifulSoup as bs    # bibliothèque pour l’interprétation du document.HTML
import pandas as pd                    # manipulation de données
import sqlite3                         # pour la création de l’instance de base de données.

def movies_scrap():
    # Initialisation
    url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
    df = pd.DataFrame(columns=["average_rank","film","year"])

    # HTTPS GET
    r = requests.get(url) 
    html_page = r.text
    soup = bs(html_page, 'html.parser')

    tables = soup.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"average_rank": col[0].contents[0],
                            "film": col[1].contents[0],
                            "year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)

    # Nom de la base de données et de la table
    db_name = '../data/movies.db'
    table_name = 'top_film'

    # Se connecter à la base de données SQLite
    conn = sqlite3.connect(db_name)

    # Insérer le DataFrame dans une table SQLite
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Fermer la connexion à la base de données
    conn.close()
    return df

