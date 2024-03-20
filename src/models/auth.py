from src.models.base import BaseModel
from src.exs import db
from flask_login import UserMixin


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    balance = db.Column(db.Integer,default=0)
    email = db.Column(db.String)
    password = db.Column(db.String)