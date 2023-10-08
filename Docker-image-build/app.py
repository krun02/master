from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!, This is kiran, learning the docker image build'