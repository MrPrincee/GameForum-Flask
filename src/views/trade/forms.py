from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired


class Trade(FlaskForm):
    current_user_items = SelectField("Your Items")
    other_user_items = SelectField("His Available Items")
    submit = SubmitField("Submit")


class ChooseUser(FlaskForm):
    all_users = SelectField("Choose")
    submit = SubmitField("Submit")