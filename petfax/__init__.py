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
    from .blueprints import pet

    #register blueprint
    app.register_blueprint(pet.bp)

    #import pet blueprint
    from .blueprints import fact

    #register blueprint
    app.register_blueprint(fact.bp)

    #return the app
    return app