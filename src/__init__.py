from flask import Flask
from src.exs import db, login_manager, mail
from src.config import Config
from src.models import User, Item, Message, Channel,SellItems
from src.admin import admin
from src.views import main_blueprint, auth_blueprint, channel_blueprint, offer_blueprint, trade_blueprint,sell_blueprint
from src.commands import init_db,test_mail

from flask_admin.contrib.sqla import ModelView
#
BLUEPRINTS = [main_blueprint, auth_blueprint, channel_blueprint, offer_blueprint, trade_blueprint,sell_blueprint]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.cli.add_command(init_db)
    reg_ext(app)
    reg_blueprint(app)
    # reg_bcrypt(app)
    return app


def reg_ext(app):
    #Sqlalchemy
    db.init_app(app)

    app.cli.add_command(init_db)
    app.cli.add_command(test_mail)

    admin.init_app(app)
    admin.add_view(ModelView(User, db.session,name="User_panel",endpoint="userpanel"))
    admin.add_view(ModelView(Item, db.session,name="Product_panel",endpoint="productpanel"))
    admin.add_view(ModelView(Message, db.session,name="Message_panel",endpoint="messagepanel"))
    admin.add_view(ModelView(Channel, db.session,name="Channel_panel",endpoint="channelpanel"))

    #login-manager
    login_manager.init_app(app)

    #flask-mail
    mail.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


# def reg_bcrypt(app):
#     Bcrypt.init_app(app)

def reg_blueprint(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)