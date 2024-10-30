import pickle
import numpy as np

def main():
    # Load the DictVectorizer and model
    with open('dv.bin', 'rb') as f:
        dv = pickle.load(f)

    with open('model1.bin', 'rb') as f:
        model = pickle.load(f)

    # Client data to score
    client_data = {"job": "management", "duration": 400, "poutcome": "success"}

    # Transform the client data using the DictVectorizer
    X_client = dv.transform([client_data])

    # Make a prediction
    prediction = model.predict(X_client)

    # Get the prediction probability 
    prediction_proba = model.predict_proba(X_client)

    # Output the results
    print("Prediction:", prediction[0])
    print("Prediction Probability:", prediction_proba[0])


if __name__ == "__main__":
    main()
