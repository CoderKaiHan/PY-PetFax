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
    return render_template('pets/index.html', pets = pets)

#Add a new pet route(Create)
@bp.route('/new')
def new():
    return render_template('pets/new_pet.html')

#Show a pet route(Read)
@bp.route('/<int:pet_id>')
def show(pet_id):
    return render_template('pets/show_pet.html', pet = pets[pet_id])
