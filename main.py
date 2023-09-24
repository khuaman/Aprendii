from flask import Flask, jsonify, request
import awsgi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def GetMessage():
    return jsonify({
        "status": "SUCESS"
    })
