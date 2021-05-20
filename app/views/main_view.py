from flask import Blueprint, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('todo.todolists'))