from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from sklearn import tree
import numpy as np
import pickle as p

app = Flask(__name__)

api = Api(app)

class Home(Resource):
    def get(self):
        j_data = request.get_json()
        prediction = np.array2string(model.predict(j_data))
        return jsonify(prediction)

api.add_resource(Home, '/')

if __name__ == '__main__':
    modelfile = 'predict_app/models/final_prediction.pickle'    
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)