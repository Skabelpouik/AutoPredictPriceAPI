import requests, json
import pickle as p
import pandas as pd
import numpy as np

url = 'http://127.0.0.1:5000/'

# Chargement du fichier contenant les données de test
testfile = 'predict_app/models/voiture_model_X_test.pkl'
data = p.load(open(testfile, 'rb'))
# Transformation du Dataframe sous forme de liste
data = data.values.tolist()
# Transformation de la liste au format JSON
j_data = json.dumps(data)
# Envoi de la requête vers le serveur flask localhost
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.get(url, data=j_data, headers=headers)
print(r,r.text)