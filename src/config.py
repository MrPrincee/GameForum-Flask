from flask import Flask
from os import path


class Config:
    app = Flask(__name__)
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY ="argetyvii"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_USERNAME = "792844df3f250e"
    MAIL_NAME = "ototest@gmail.com"
    MAIL_PASSWORD = "d2dc5daa368875"
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    


