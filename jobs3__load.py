import pandas as pd                 # Manipulation de données
import sqlite3                      # pour la création de l’instance de base de données.

# Load data to .csv
def load(target_file, transformed_data):
    transformed_data.to_csv(target_file)

# Historisation des chargement
def history(target_file, transformed_data, time):
    transformed_data.to_csv(time+ "-" + target_file)
# Load data to .json

# Load data to .db sqlite


"""# Nom de la base de données et de la table
db_name = '../data/movies.db'
table_name = 'top_film'

# Se connecter à la base de données SQLite
conn = sqlite3.connect(db_name)

# Insérer le DataFrame dans une table SQLite
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Fermer la connexion à la base de données
conn.close()"""
