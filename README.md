# Duplicate Question Pairs Predictor 

This is the backend service for the **Duplicate Question Pairs Predictor** project. It is built using Flask and provides an API endpoint for predicting whether two questions are duplicates.

---

## Features

- Accepts two questions via a POST request.
- Uses a pre-trained machine learning or deep learning model to predict if the questions are duplicates.
- Returns a JSON response with the prediction result.
- Handles CORS for cross-origin requests from the frontend.

---

## Technologies Used

- **Flask**: Python web framework for building the backend API.
- **Flask-CORS**: To handle cross-origin requests.
- **Python Libraries**: 
  - `numpy`, `pandas`: For data manipulation.
  - `joblib` or `pickle`: For loading the pre-trained model.

---

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (v3.7 or higher)
- pip (comes with Python) or a virtual environment manager (e.g., `venv` or `conda`)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/duplicate-question-pairs-backend.git
   cd duplicate-question-pairs-backend

2. **Create a virtual environment**:
   ```bash
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate     # For Windows
   
3. **Install dependencies**:
    ```bash
        pip install -r requirements.txt

4. **Add your model file**:

   Place the pre-trained model file (model.pkl or equivalent) in the model/ directory.

6. **Run the server**:
   ```bash
     python app.py

7. **Access the API**:
   
   The API will be available at http://127.0.0.1:5000/predict.

# API Documentation

## Endpoint: `/predict`

### Method: `POST`

### Request Body:
Send a JSON object with the following fields:

 ```json
            {
                "question1": "string",
                "question2": "string"
            }
