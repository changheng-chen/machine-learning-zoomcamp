import requests

# Define the URL of your Flask app
url = "http://localhost:8000/score"  # Adjust the endpoint as necessary

# Client data to score
client = {"job": "management", "duration": 400, "poutcome": "success"}

# Send POST request and get the response
response = requests.post(url, json=client)

# Print the response
print(response.json())
