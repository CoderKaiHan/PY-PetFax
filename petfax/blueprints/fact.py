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
    
    #below is GET request
    #Query all facts from the database
    results = models.Fact.query.all()
    #loop through results to check if the query is successful
    for result in results:
      print(result) #we got the output like this <Fact ID#> (This is an object. We can access the attributes of the object like this: result.submitter, result.fact) This for-loop can be deleted.

    return render_template('facts/index.html', facts = results)

#Add a new fun fact(Create)
@bp.route('/new')
def new():
    return render_template('facts/new_fun_fact.html')
