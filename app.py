from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, this is a test web app based on python!'