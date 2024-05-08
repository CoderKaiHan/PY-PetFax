from flask import Blueprint

bp = Blueprint(
    'pet', 
    __name__ ,
    url_prefix='/pets'
    )

@bp.route('/')
def index():
    return 'Hello, this is pets index!!!'