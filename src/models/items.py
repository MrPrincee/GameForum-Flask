from src.models.base import BaseModel
from src.exs import db


class Item(BaseModel):
    __tablename__ = "items"

    name = db.Column(db.String)
    id = db.Column(db.Integer,primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    price = db.Column(db.Integer)


