from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField

from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

class PostForm(FlaskForm):
    title = StringField('title', [DataRequired(), Length(max=255)])
    subtitle = StringField('subtitle')
    content = TextAreaField('content', [DataRequired()])