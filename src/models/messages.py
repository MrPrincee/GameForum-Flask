from src.models.base import BaseModel
from src.exs import db


class Message(BaseModel):
    __tablename__ = "messages"

    name = db.Column(db.String,db.ForeignKey("users.name"))
    id = db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))
