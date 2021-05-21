from todo import db

class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    author = db.Column(db.String(200), nullable = False)
    create_data = db.Column(db.String(200), nullable = False)

class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key = True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todolist.id', ondelete='CASCADE'))
    todo = db.relationship('TodoList', backref = db.backref('reply_set'))
    content = db.Column(db.Text(), nullable = False)
    author = db.Column(db.String(200), nullable = False)
    create_data = db.Column(db.String(200), nullable = False)
