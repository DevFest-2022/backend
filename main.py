from flask import Flask
import hi

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<username>')
def main(username):
    return hi.finalfunction(username)