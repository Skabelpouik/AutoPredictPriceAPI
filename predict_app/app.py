from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import numpy as np
import pickle as p
from joblib import load

app = Flask(__name__) # Flask app instance initiated

api = Api(app) # Flask restful wraps Flask app around it.

class Home(Resource):
    def get(self):
        """
        Prédit le prix d'une voiture d'occasion
        Retourne le montant de la prédiction
        """
        # Récupération de la requête au format JSON
        j_data = request.get_json()
        # Résultat de la prédiction d'une ligne du fichier reçu en requête stocké dans un numpyarray
        prediction = np.array2string(model.predict(j_data[:1]))
        #prediction = np.array2string(pipeline.predict(j_data))
        return jsonify(prediction)

api.add_resource(Home, '/')

if __name__ == '__main__':
    # Chargement du modèle via pickle
    modelfile = 'predict_app/models/voiture_model_RFR.pkl'    
    model = p.load(open(modelfile, 'rb'))
    #pipeline = load("predict_app/models/text_classification.joblib")
    # Lancement de l'application
    app.run(debug=True)