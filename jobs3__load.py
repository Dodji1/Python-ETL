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
