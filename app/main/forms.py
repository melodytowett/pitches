from turtle import title
from unicodedata import category
from urllib.request import Request
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class Pitchform(FlaskForm):
    title = StringField('Enter your pitche title',validators=[DataRequired()])
    category = SelectField('Enter Pitch Category',validators=[DataRequired])
    content = StringField('Describe the pitch',validators=[DataRequired])
    submit = SubmitField('submit Pitch')
