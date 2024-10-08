from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Message": "Welcome to Tax Break!"})


API_KEY = "11b598581fe6442c806e697800d18ed3"
RENTCAST_URL = "https://api.rentcast.io/v1/properties"


@app.route('/address/<string:address>', methods=['GET'])
def get_address(address):
    print(f"Received address: {address}")

    # Prepare the request to Rentcast API
    headers = {
        "X-Api-Key": API_KEY,
        "accept": "application/json"
    }
    params = {
        "address": address
    }

    try:
        # Make the request to Rentcast API
        response = requests.get(RENTCAST_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Get the JSON data from the response
        data = response.json()

        # Return the data as a JSON response
        return jsonify(data)
    except requests.RequestException as e:
        # Handle any errors that occurred during the request
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5050))
