
import joblib
import numpy as np

model = joblib.load("model.joblib")

def predict_price(data:dict):
    
    feature = np.array([
        [
            data['area'],
            data['bedrooms'],
            data['bathrooms'],
            data['stories'],
            data['parking']
        ]
        ])
    
    return  model.predict(feature)