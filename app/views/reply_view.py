from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from todo import db
from app.models.todo import TodoList, Reply
from app.views.forms import ReplyForm

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route('/create/<int:todo_id>', methods = ['POST'])
def reply_create(todo_id):
    todo = TodoList.query.get_or_404(todo_id)
    content = request.form['content']
    reply = Reply(content = content, create_data = datetime.now())
    todo.reply_set.append(reply)
    db.session.commit()
    return redirect(url_for('todo.todo_detail', todo_id = todo_id))

@bp.route('modify/<int:reply_id>', methods = ['GET', 'POST'])
def reply_modify(reply_id):
    reply = Reply.query.get_or_404(reply_id)
    if request.method == 'POST':
        form = ReplyForm()
        if form.validate_on_submit():
            form.populate_obj(reply)
            db.session.commit()
            return redirect(url_for('todo.todo_detail', todo_id = reply.todo.id))
    else: form = ReplyForm(obj = reply)
    return render_template('reply/reply_form.html', reply = reply, form = form)

@bp.route('/delete/<int:reply_id>')
def reply_delete(reply_id):
    reply = Reply.query.get_or_404(reply_id)
    todo_id = reply.todo.id
    db.session.delete(reply)
    db.session.commit()
    return redirect(url_for('todo.todo_detail', todo_id = todo_id))