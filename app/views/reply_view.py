from datetime import datetime
from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
from todo import db
from app.models.todo import TodoList, Reply

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route('/create/<int:todo_id>', methods=('POST'))
def create(todo_id):
    todo = TodoList.query.get_or_404(todo_id)
    content = request.form['content']
    reply = Reply(content = content, create_date = datetime.now())
    todo.reply_set.append(reply)
    db.session.commit()
    return redirect(url_for('todo.todo_detail', todo_id = todo_id))