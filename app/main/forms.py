from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Enter your pitche title',validators=[DataRequired()])
    category = SelectField('Enter Pitch Category',choices=[('Promotion','Promotion'),('Motivation','Motivation'),('Technology','Technology'),('Religion','Religion')],validators=[DataRequired()])
    content = TextAreaField('Describe the pitch',validators=[DataRequired])
    submit = SubmitField('submit Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Descrie your self', validators=[DataRequired()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    Comment = TextAreaField('comments',validators=[DataRequired()])
    submit = SubmitField('content')

