from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo


class Register_Form(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname")
    email = EmailField("Email")
    password = PasswordField("Password")
    conf_password = PasswordField("Confirm Password", validators=[EqualTo("password", message="Must be equal!")])
    submit = SubmitField("Submit")


class Login_Form(FlaskForm):
    email = EmailField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Submit")


class Add_Balance(FlaskForm):
    balance = IntegerField("Balance")
    submit = SubmitField('Submit')