from flask import ( Blueprint, render_template, request, redirect )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint(
    #name of the blue print
    'fact', 
    #name of the current module
    __name__ ,
    #url prefix
    url_prefix='/facts'
    )

#index route, show all pets(Read)
@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
      print (request.form)
      return redirect('/facts')
    
    return render_template('facts/index.html', pets = pets)

#Add a new fun fact(Create)
@bp.route('/new')
def new():
    return render_template('facts/new_fun_fact.html')
