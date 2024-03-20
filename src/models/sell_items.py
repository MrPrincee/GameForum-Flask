from src.models.base import BaseModel
from src.exs import db


class SellItems(BaseModel):
    id = db.Column(db.Integer,primary_key=True)
    item_id = db.Column(db.Integer,db.ForeignKey('items.id'))
    name = db.Column(db.String, db.ForeignKey("items.name"))
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer,db.ForeignKey("items.owner_id"))