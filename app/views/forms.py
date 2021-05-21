from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    label = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class ReplyForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])