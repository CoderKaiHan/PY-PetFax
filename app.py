#configureation
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is PetFax!'

@app.route('/pets')
def pets():
    return 'These are our cool pets available for adoption!'