import search
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<handle>')
def main(handle):
    search_dict = search.favorite_users(
        handle=handle, 
        max_processed_tweets=10, 
        max_results=5)
    
    response = jsonify(search_dict)
    response.status_code = 200
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response