from flask import ( Blueprint, render_template, request, redirect )
import json
#import models
from ..models import models

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

      #set the variables with the form data  received
      submitter = request.form['submitter']
      fact = request.form['fun_fact']
      #create a new fact instance from Fact model
      new_fact = models.Fact(submitter = submitter, fact = fact)
      #add new_fact to the Flask-SQLAchemy database session
      models.db.session.add(new_fact)
      #Commit the database session(insert into database)
      models.db.session.commit()
      
      return redirect('/facts')
    
    return render_template('facts/index.html', pets = pets)

#Add a new fun fact(Create)
@bp.route('/new')
def new():
    return render_template('facts/new_fun_fact.html')
