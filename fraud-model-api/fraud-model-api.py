# Dependencies
from flask import Flask, request, jsonify
import pickle
import traceback
import pandas as pd
import numpy as np
import sys

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.fillna(0) # fill na's values with zero
            query = query.reindex(columns=model_columns, fill_value=0) # looks like a dataframe

            prediction = list(model.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 12345  # If you don't provide any port the port will be set to 12345

    model = pickle.load(open('SGD_fraud_v01.pkl', 'rb')) # Load "model.pkl"
    print('Model loaded')
    model_columns = pickle.load(open('SGD_fraud_v01_columns.pkl', 'rb')) # Load "model_columns.pkl"
    print('Model columns loaded')

    app.run(port=port, debug=True)