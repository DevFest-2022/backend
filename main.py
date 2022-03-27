from flask import Flask
import search

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<handle>')
def main(handle):
    return search.favorite_users(handle)