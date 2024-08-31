import pandas as pd                 # Manipulation de données

# Convertion
def transform(data):
    '''Convertion de inches to metre et arrondir de deux décimals
    1 inch = 0.0254 m '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convertion de pounds to kilogrammes et arrondir de deux décimals
    1 pound = 0.45359237 kg '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data

# Nom première lettre en majuscule



