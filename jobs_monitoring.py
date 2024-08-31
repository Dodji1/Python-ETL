from jobs1_extract import extract      # fonction extract pour l'opération d'extraction des données
from jobs2_transform import transform  # fonction transform pour l'opération d'transformation des données
from jobs3_load import load            # fonction load pour l'opération de chargement des données
from datetime import datetime          # gestion de temps pour le suivie des opérations

log_file = r"data\log_file.txt"
target_file_csv = r"data\transformed_data.csv"

# Suivi de l'exécultion des taches
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format)
    with open(log_file,"a") as f:
        f.write(timestamp + ',' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started")
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract()
 
# Log the completion of the Extraction process
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data) 
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process 
log_progress("Transform phase Ended")
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load(target_file_csv,transformed_data)

# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 