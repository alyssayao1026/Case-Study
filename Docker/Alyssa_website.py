import joblib
import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
num_models = 13
MLP_Final = []
for i in range(0, num_models):
    model_path = os.path.join("Model", f'model_{i}.joblib')
    loaded_model = joblib.load(model_path)
    MLP_Final.append(loaded_model)
    
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = ['Month', 'CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)', 'T', 'RH', 'AH']
    inputs = {}
    prediction_type = request.json.get('selected-prediction-type')
    for feature in features:
        value = request.json.get(feature)
        if value is None:
            if feature == prediction_type or feature == "Month":
                continue
            return jsonify({'error': f'Missing value for feature {feature}.'}), 400
        inputs[feature] = float(value)  

    Scalers = []
    for i in range(0, num_models): 
        scaler_path = os.path.join("Scaler", f'scaler_{i}.joblib') 
        scaler = joblib.load(scaler_path)
        Scalers.append(scaler)

    scaler_index = features.index(prediction_type) - 1
    Scaler = Scalers[scaler_index]

    scaled_inputs = Scaler.transform(np.array([list(inputs.values())]))

    
    model_index = features.index(prediction_type) - 1
    model = MLP_Final[model_index]
    try:
        prediction = model.predict(scaled_inputs)[0]
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': f'Error predicting: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")