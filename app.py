#!flask/bin/python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return str(random.randint(0,10))

if __name__ == '__main__':
    app.run(debug=True)
