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

#index route, show all pets(Read)
@bp.route('/')
def index():
    return render_template('index.html', pets = pets)

#Add a new pet route(Create)
@bp.route('/new')
def new():
    return render_template('new_pet.html')

#Show a pet route(Read)
@bp.route('/<int:pet_id>')
def show(pet_id):
    return render_template('show_pet.html', pet = pets[pet_id])

#Create a new facts for a pet
@bp.route('/new_fun_fact')
def new_fun_fact():
    return render_template('new_fun_fact.html')