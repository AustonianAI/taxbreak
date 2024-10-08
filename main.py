from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"welcome to tax break! 🚅"})


@app.route('/address/<string:address>', methods=['GET'])
def get_address(address):
    print(f"Received address: {address}")
    return f"Address received: {address}"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
