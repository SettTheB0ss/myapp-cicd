from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker! This is my Flask app running in a container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
