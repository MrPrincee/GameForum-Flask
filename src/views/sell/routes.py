from flask import render_template, Blueprint, redirect, url_for, request

from flask_login import current_user

from src.views.sell.forms import Sell_Form

from src.models import SellItems, Item, User

sell_blueprint = Blueprint("sell", __name__)


@sell_blueprint.route("/market",methods=["POST","GET"])
def market():
    selling_items = SellItems.query.all()

    return render_template("sell/market.html", selling_items=selling_items)


@sell_blueprint.route("/buy_item/<int:item_id>",methods=["POST","GET"])
def buy_item(item_id):
    selling_item = SellItems.query.filter_by(id=item_id).first()
    buyer = User.query.filter_by(id=current_user.id).first()
    item = Item.query.filter_by(id=selling_item.item_id).first()

    if selling_item and buyer.balance >= selling_item.price:
        item.owner_id = buyer.id
        item.save()
        buyer.balance = buyer.balance - selling_item.price
        buyer.save()
        selling_item.delete()
    else:
        return redirect(url_for("sell.market"))
    return redirect(url_for("sell.market"))


@sell_blueprint.route("/add_item", methods=["POST", "GET"])
def add_item():
    form = Sell_Form()
    current_user_items = Item.query.filter_by(owner_id=current_user.id).all()
    items_on_sale = [sell_item.item_id for sell_item in SellItems.query.all()]

    current_user_items = [item for item in current_user_items if item.id not in items_on_sale]

    form.item.choices = [(item.id, item.name) for item in current_user_items]

    if form.validate_on_submit():
        item = Item.query.filter_by(id=form.item.data).first()
        add_item = SellItems()
        add_item.item_id = item.id
        add_item.name = item.name
        add_item.price = form.price.data
        add_item.owner_id = item.owner_id
        add_item.create()
        return redirect(url_for("sell.market"))

    return render_template("sell/add_item.html", form=form)


@sell_blueprint.route("/delete_item/<int:item_id>", methods=["POST","GET"])
def delete_item(item_id):
    item = SellItems.query.filter_by(id=item_id).first()
    item.delete()
    item.save()
    return redirect(url_for("sell.market"))

