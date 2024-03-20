from src.models.base import BaseModel
from src.exs import db


class Channel(BaseModel):
    __tablename__ = "channels"

    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    channel_admin = db.Column(db.Integer)