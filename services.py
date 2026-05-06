import json
import os

def get_all_calls():
    # Βρίσκουμε τον φάκελο που είναι το services.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Αν το αρχείο είναι π.χ. στον υποφάκελο 'data', το προσθέτεις εδώ:
    # file_path = os.path.join(base_dir, 'Ο_ΦΑΚΕΛΟΣ_ΣΟΥ', 'calls.json')
    file_path = os.path.join(base_dir, 'data', 'calls.json') 
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

print(get_all_calls())
