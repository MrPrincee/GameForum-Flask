import datetime
import secrets

from flask import render_template, Blueprint, redirect, url_for, session,abort,flash

from src.utils import send_mail

from flask_login import login_user

from flask_login import current_user

from src.views.trade.forms import Trade, ChooseUser

from src.models import User, Item, SellItems



from src.exs import db

trade_blueprint = Blueprint("trade", __name__)

other_user_id = None


@trade_blueprint.route("/create_trade",methods=["POST","GET"])
def create_trade():
    global other_user_id

    if other_user_id == None:
        return redirect(url_for("trade.choose_user"))
    else:
        form = Trade()
        other_user_sell_item = SellItems.query.filter_by(owner_id=other_user_id).all()
        other_user_items = Item.query.filter_by(owner_id=other_user_id)
        other_user_sell_item_id = []

        for item in other_user_sell_item:
            other_user_sell_item_id.append(item.item_id)

        form.other_user_items.choices = [(item.id,item.name) for item in other_user_items if item.id not in other_user_sell_item_id]

        current_user_item = Item.query.filter_by(owner_id=current_user.id)
        current_user_sell_item = SellItems.query.filter_by(owner_id=current_user.id).all()
        current_user_sell_item_id = []

        for item in current_user_sell_item:
            current_user_sell_item_id.append(item.item_id)

        form.current_user_items.choices = [(item.id,item.name) for item in current_user_item if item.id not in current_user_sell_item_id]

        if form.validate_on_submit():
            other_user = User.query.filter_by(id=other_user_id).first()
            html = render_template("trade/_trade_mail.html")
            send_mail("Trade",html, [other_user.email])

            session['current_user_item'] = form.current_user_items.data
            session['other_user_item'] = form.other_user_items.data
            return redirect(url_for("main.about"))

        return render_template("trade/create_trade.html", form=form)


@trade_blueprint.route("/choose_user",methods=["POST","GET"])
def choose_user():
    global other_user_id

    form = ChooseUser()

    all_users = User.query.all()

    if current_user.is_authenticated:
        for user in all_users:
            if user.id == current_user.id:
                all_users.remove(user)
    else:
        return redirect(url_for('auth.login'))

    form.all_users.choices = [(user.id, user.name) for user in all_users]

    if form.validate_on_submit():
        other_user_id = form.all_users.data
        return redirect(url_for("trade.create_trade"))

    return render_template("trade/choose_user.html",form=form)


@trade_blueprint.route("/accept_trade",methods=["POST","GET"])
def accept_trade():
    global other_user_id
    first_item_id = session.get('current_user_item')
    second_item_id = session.get('other_user_item')

    first_item = Item.query.get(first_item_id)
    second_item = Item.query.get(second_item_id)


    if other_user_id== None:
        abort(403, "Trade is already declined or link is expired")

    first_owner = first_item.owner_id
    second_owner = second_item.owner_id

    log_user = User.query.filter_by(id=first_owner).first()

    first_item.owner_id = second_owner
    second_item.owner_id = first_owner

    db.session.commit()

    session.clear()
    other_user_id = None
    login_user(log_user)

    return "Trade Accepted!"


@trade_blueprint.route("/decline_trade",methods=["POST","GET"])
def decline_trade():
    global other_user_id

    if other_user_id:
        log_user = User.query.filter_by(id=current_user.id).first()
        session.clear()
        other_user_id = None
        login_user(log_user)
        return "Trade Declined!"
    else:
        abort(403, "Trade is already declined or link is expired")