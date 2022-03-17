import requests, json
import pickle as p

url = 'http://127.0.0.1:5000/'

#data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]
#data = ["@user @user lumpy says i am a . prove it lumpy."]
testfile = 'predict_app/models/voiture_model_LR.pkl'    
data = p.load(open(testfile, 'rb'))
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.get(url, data=j_data, headers=headers)
print(r,r.text)