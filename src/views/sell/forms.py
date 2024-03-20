from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired


class Sell_Form(FlaskForm):
    item = SelectField("Select")
    price = IntegerField("Price")
    submit = SubmitField("Submit")