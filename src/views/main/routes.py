from flask import render_template, Blueprint, redirect, url_for


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/about")
def about():
    return render_template("main/about_us.html")


@main_blueprint.route("/")
def start():
    return redirect(url_for("main.about"))


