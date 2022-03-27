from flask import Flask
import search

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<username>')
def main(username):
    return search.finalfunction(username)