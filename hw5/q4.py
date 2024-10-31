import pickle
from flask import Flask, request, jsonify

# Load the DictVectorizer and model
with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)

with open('model1.bin', 'rb') as f:
    model = pickle.load(f)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    # Get the JSON data from the request
    client_data = request.get_json()

    # Transform the client data using the DictVectorizer
    X_client = dv.transform([client_data])

    # Make a prediction
    prediction = model.predict(X_client)
    prediction_proba = model.predict_proba(X_client)

    # Prepare the response
    response = {
        'prediction': int(prediction[0]),
        'probability': prediction_proba[0].tolist()  # Convert to list for JSON serialization
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

# run app with gunicorn
# pipenv run gunicorn --bind 0.0.0.0:8000 q4:app
