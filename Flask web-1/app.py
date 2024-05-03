from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Use jsonify to create a JSON response
    return jsonify({"message": "helloworld"})
