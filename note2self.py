from flask import Flask
from flask_cors import CORS
from flask import jsonify

from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

import re
import sys
import tensorflow as tf
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()

