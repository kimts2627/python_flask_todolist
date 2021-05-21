from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from app.models.todo import TodoList
from todo import db
from werkzeug.utils import redirect
from app.views.forms import TodoForm

bp = Blueprint('todo', __name__, url_prefix='/')

@bp.route('/todolists')
def todolists():
    page = request.args.get('page', type = int, default = 1)
    todo_list = TodoList.query.order_by(TodoList.create_data.desc())
    todo_list = todo_list.paginate(page, per_page = 10)
    return render_template('todo/todo_list.html', todo_list = todo_list)

@bp.route('/todolists/detail/<int:todo_id>')
def todo_detail(todo_id):
    todo = TodoList.query.get_or_404(todo_id)
    return render_template('todo/todo_detail.html', todo = todo)

@bp.route('/todolists/create', methods=['GET', 'POST'])
def todo_create():
    form = TodoForm()
    if request.method == 'POST' and form.validate_on_submit():
        todo = TodoList(label = form.label.data, content = form.content.data, author = form.author.data, create_data = datetime.now())
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.todolists'))
    return render_template('todo/todo_form.html', form = form)

@bp.route('/todolists/delete/<int:todo_id>')
def todo_delete(todo_id):
    target = TodoList.query.get_or_404(todo_id)
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('todo.todolists'))

@bp.route('/todolists/modify/<int:todo_id>', methods=['GET', 'POST'])
def todo_modify(todo_id):
    target = TodoList.query.get_or_404(todo_id)
    if request.method == 'POST':
        form = TodoForm()
        if form.validate_on_submit():
            form.populate_obj(target)
            db.session.commit()
            return redirect(url_for('todo.todo_detail', todo_id = todo_id))
    else:
        form = TodoForm(obj=target)
    return render_template('todo/todo_form.html', form = form)
