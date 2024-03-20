from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired,length,Email, EqualTo

class Message_Form(FlaskForm):
    name = StringField("name")
    message = StringField("Message",validators=[DataRequired()])
    submit = SubmitField("Submit")
