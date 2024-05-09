from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint(
    #name of the blue print
    'pet', 
    #name of the current module
    __name__ ,
    #url prefix
    url_prefix='/pets'
    )

#index route
@bp.route('/')
def index():
    return render_template('index.html', pets = pets)

#test route
@bp.route('/test')
def test():
    return 'This is a test route!'