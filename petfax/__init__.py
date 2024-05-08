#import flask
from flask import Flask

#Flask app factory
def create_app():
    #create and configure the app(Flask instance)
    app = Flask(__name__)

    #index route
    @app.route('/')
    def index():
        return 'Hello, this is PetFax!!!'
    
    #import pet blueprint
    from . import pet

    #register blueprint
    app.register_blueprint(pet.bp)

    #return the app
    return app