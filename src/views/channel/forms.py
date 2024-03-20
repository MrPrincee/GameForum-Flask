from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField
from wtforms.validators import DataRequired


class Channel_Form(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    submit = SubmitField("Submit")
