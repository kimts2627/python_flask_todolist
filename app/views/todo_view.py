from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/')

@bp.route('/')
def index():
    return "main"

@bp.route('/todo')
def hello():
    return "hello todo"