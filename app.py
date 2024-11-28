from flask_cors import CORS 
from flask import  Flask , jsonify , request
import pickle
import numpy as np
import helper
import sklearn
import os

app = Flask(__name__)
CORS(app, resources={r"/predict/*": {"origins": "*"}})  # Allow requests from frontend

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)



# Route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    question1 = data.get('question1', '')
    question2 = data.get('question2', '')

    # Process question to vector
    query = helper.query_point_creator(question1,question2)
    
    # Get prediction
    prediction = model.predict(query)
    # prediction = prediction.tolist() 
    prediction = prediction.tolist() if hasattr(prediction, 'tolist') else prediction
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))