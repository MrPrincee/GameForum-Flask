from flask.cli import with_appcontext
import click
from flask import Flask

from src.models import User,Item
from src.exs import db

from src.utils import send_mail

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    new_user = User(id=1,name="oto",surname="jojishvili",balance=0,email="otar.jojishvili.1@btu.edu.ge",password="k")
    new_user2 = User(id=2, name="zura", surname="zuriko", balance=0, email="otojojishvili@gmail.com",password="k")

    new_user.create()
    new_user2.create()

    new_item = Item(name="M4",id=1,owner_id=1,price=500)
    new_item2 = Item(name="Sniper", id=2, owner_id=2, price=500)
    new_item3 = Item(name="Desert Eagle", id=3, owner_id=1, price=500)
    new_item4 = Item(name="Knife", id=4, owner_id=2, price=500)

    new_item.create()
    new_item2.create()
    new_item3.create()
    new_item4.create()

    click.echo("Done!")







