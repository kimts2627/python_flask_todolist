from todo import db

class TodoList(db.Model):
    # __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_data = db.Column(db.DateTime(), nullable=False)