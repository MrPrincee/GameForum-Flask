from flask_mail import Message

from src.config import Config

from src.exs import mail


def send_mail(subject, html, recipients):
    message = Message(subject=subject, html=html, recipients=recipients,sender=Config.MAIL_NAME)
    mail.send(message)




