from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/likes')
def likes():
    return "List of all liked users should go here!"