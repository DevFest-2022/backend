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

@app.route('/partial/<query>')
def search_user(query):
    search.users(query=query)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    