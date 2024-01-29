import re
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_medicine_names(input_string, medicine_names):
    pattern = r'\b(?:' + '|'.join(re.escape(name.lower()) for name in medicine_names) + r')\b'
    extracted_names = re.findall(pattern, input_string.lower(), flags=re.IGNORECASE)
    return extracted_names

def pratham(input_text, dataset1, dataset2, dataset3):
    detected_diseases = ''
    detected_surgery = ''
    detected_symptoms = []
    detected_tests = []

    # Check for diseases and symptoms in the input text
    for _, row in dataset1.iterrows():
        disease = str(row['Disease']).lower()
        if disease in input_text.lower():
            detected_diseases = disease

    # Check for symptoms in the input text
    for _, row in dataset2.iterrows():
        symptom = str(row['Symptom']).lower()
        if symptom in input_text.lower():
            detected_symptoms.append(symptom)

    # Check for past or potential surgeries in the input text
    for _, row in dataset3.iterrows():
        surgery = str(row['surgery']).lower()
        if surgery in input_text.lower():
            detected_surgery = surgery

    # Check for past or potential tests in the input text
    for _, row in dataset3.iterrows():
        tests = str(row['test']).lower()
        if tests in input_text.lower():
            detected_tests.append(tests)

    detected_symptoms = list(set(detected_symptoms))
    detected_tests = list(set(detected_tests))

    result = {
       'detected_diseases': detected_diseases,
       'detected_symptoms' : detected_symptoms,
       'detected_surgery' : detected_surgery,
       'detected_tests' : detected_tests
    }
    return result

def gladys(input_text, medicines_dataset, immunization_dataset):
    # Initialize columns
    regular_medicines = set()
    last_prescribed_medicines = set()
    current_prescribed_medicines = set()
    immunization_history = set()

    # Split the text into sentences
    sentences = [sentence.lower() for sentence in input_text.split('. ')]

    # Iterate through the sentences
    for sentence in sentences:
        print('Sent:', sentence)
        # Check for regular, last prescribed, and current prescribed medicines
        if "regularly taking" in sentence:
            print('Sentence : ' + sentence)
            for medicine in medicines_dataset:
                if extract_medicine_names(sentence, medicines_dataset):
                    regular_medicines.add(medicine)
        elif "last time" in sentence:
            for medicine in medicines_dataset:
                if extract_medicine_names(sentence, medicines_dataset):
                    last_prescribed_medicines.add(medicine)
        elif "currently taking" in sentence:
            for medicine in medicines_dataset:
                if extract_medicine_names(sentence, medicines_dataset):
                    current_prescribed_medicines.add(medicine)
        else:    # Check for immunization
            for immunization in immunization_dataset:
                if extract_medicine_names(sentence, immunization_dataset):
                    immunization_history.add(immunization)

    # Convert sets to lists
    regular_medicines = list(regular_medicines)
    last_prescribed_medicines = list(last_prescribed_medicines)
    current_prescribed_medicines = list(current_prescribed_medicines)
    immunization_history = list(immunization_history)

    result = {
        'regular_medicines' : regular_medicines,
        'last_prescribed_medicines' : last_prescribed_medicines,
        'current_prescribed_medicines' : current_prescribed_medicines,
        'immunization_history' : immunization_history
    }

    return result

input_text = "! Hello Doctor, my name is Gladys. I am 21 years old and female. I have been experiencing persistent cough, high fever and fatigue for the past few days. I got my influenza vaccine a couple of months ago. Hello Gladys, based on your symptoms and recent influenza vaccination, it is likely that you have hypertension. Do you have any underlying health conditions? Are you currently taking any medications? I recently had a bypass surgery. I am regularly taking CTZ tablet. Last time you had prescribed Allegra M tablet. I would prescribe to take short mag spray every morning and keep an eye on your symptoms. Additionally I recommend a nasal swab test to confirm the hypertension diagnosis and to check for any secondary infections. If there is any worsening, contact our office immediately. Thank you doctor. I will follow your advice and get the nasal swab test done as soon as possible and buy the fist-trap medication."

dataset1 = pd.read_csv('datasets/dataset.csv')
dataset2 = pd.read_csv('datasets/Symptom-severity.csv')
dataset3 = pd.read_csv('datasets/test_surgery.csv')

medicines_df = pd.read_csv('datasets/A_Z_medicines_dataset_of_India.csv')
medicines_dataset = list(medicines_df['name'])

immunization_df = pd.read_csv('datasets/Immunization.csv', encoding='ISO-8859-1')
immunization_dataset = list(immunization_df['Vaccine'])

""" res1 = pratham(input_text, dataset1, dataset2, dataset3)
print(res1) """

import time
start_time = time.time()
print('Start Time : ',start_time)
res2 = gladys(input_text, medicines_dataset, immunization_dataset)
end_time = time.time()

print('Total Time:', end_time - start_time)
print(res2)
