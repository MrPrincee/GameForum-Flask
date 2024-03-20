from flask import render_template, Blueprint, request, redirect, url_for

from flask_login import login_user, logout_user, current_user

from src.models import User, Item
from src.views.auth.forms import Register_Form, Login_Form, Add_Balance

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=['POST', 'GET'])
def register():
    form = Register_Form()
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            new_user.create()
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/login", methods=["POST", "GET"])
def login():
    form = Login_Form()
    logged_user = User.query.filter(User.email == form.email.data).first()
    if current_user.is_authenticated:
        logout_user()
    else:
        if request.method == "POST":
            if logged_user:
                if logged_user.password == form.password.data:
                    login_user(logged_user)
                    return redirect(url_for("main.about"))

    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/profile",methods=["GET","POST"])
def profile():
    logged_user = User.query.filter_by(id=current_user.id).first()
    current_user_items = Item.query.filter_by(owner_id=current_user.id).all()

    return render_template("auth/profile.html",logged_user=logged_user,user_items=current_user_items)


@auth_blueprint.route("/add_balance/<int:user_id>",methods=["GET","POST"])
def add_balance(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = Add_Balance()
    if form.validate_on_submit():
        user.balance += form.balance.data
        user.save()
        return redirect(url_for("auth.profile"))
    return render_template("auth/add_balance.html",form=form)
