import requests

# Set the URL for the Flask app
#url = "http://127.0.0.1:5000/score"
url = "http://localhost:8000/score"

# Client data to score
client = {"job": "student", "duration": 280, "poutcome": "failure"}

# Make a POST request to the Flask app
response = requests.post(url, json=client)

# Print the response
print(response.json())
