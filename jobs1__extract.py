import glob                         # Manipulation de fichiers
import pandas as pd                 # Manipulation de données
import xml.etree.ElementTree as ET  # Manipulation de fichier xlm
from datetime import datetime       # gestion de temps

from jobs1_1_api_connect import app_extract
from jobs1_2_database_coonect import database_extract
#from jobs1_3_local_files import extract
#from jobs1_4_websscraping import movies_scrap

# Fonctions permettant d’extraire les données de différents formats de fichiers.
# .csv .json .xml .xlsx

source_fles = r"source_files"      # tous les fichiers locals

# Extraction de fichier csv
def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process)
    return dataframe

# Extraction de fichier .xlsx
def extract_from_excel(file_to_process):
    dataframe = pd.read_excel(file_to_process)
    return dataframe

# Extraction de fichier .json
def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

# Extraction de fichier .xlm
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe

# Extraction de tous les fichiers
def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data     
    # process all csv files 
    for csvfile in glob.glob(f"{source_fles}/*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)         
    # process all json files 
    for jsonfile in glob.glob(f"{source_fles}/*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)     
    # process all xml files 
    for xmlfile in glob.glob(f"{source_fles}/*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)         
    return extracted_data
