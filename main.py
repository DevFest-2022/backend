from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def main():
    username = request.args.get('username')
    return username