from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ArtistSearchForm(FlaskForm):
    search_term = StringField('Search Artist...', validators=[DataRequired()])
    submit = SubmitField('Search')