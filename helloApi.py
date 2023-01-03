import json
import requests
from flask import Flask,jsonify,request


app = Flask(__name__)
"""@app.route('/')
def index():
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com'})"""
@app.route('/', methods=['GET'])
def query_records():
    #name = request.args.get('name')
    #print (name)
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        print(records)
        for record in records:
           # if record['name'] == name:
            print(record)
            return jsonify(record)

        return jsonify({'error': 'data not found'})

app.run()