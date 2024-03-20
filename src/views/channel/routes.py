from flask import render_template, Blueprint, redirect, url_for, request

from src.models import Channel, Message
from src.views.channel.forms import Channel_Form

from flask_login import current_user


from src.views.main.forms import Message_Form

channel_blueprint = Blueprint("channel", __name__)


@channel_blueprint.route("/channel", methods=["GET"])
def channel():
    all_channels = Channel.query.all()
    return render_template("channels/channel.html", channels=all_channels)


@channel_blueprint.route("/channel_chat/<int:channel_id>", methods=['POST', 'GET'])
def channel_chat(channel_id):
    current_channel = Channel.query.filter_by(id=channel_id).first()
    channel_messages = Message.query.filter_by(channel_id=channel_id)
    channel_admin = current_channel.channel_admin
    form = Message_Form()
    if request.method == "POST" and form.validate_on_submit():
        if current_user.is_authenticated:
            new_message = Message()
            new_message.channel_id = channel_id
            form.name.data = current_user.name
            form.populate_obj(new_message)
            new_message.create()
        else:
            return redirect(url_for("auth.login"))

        return redirect(url_for("channel.channel_chat", channel_id=channel_id))

    return render_template("channels/channel_chat.html", messages=channel_messages, form=form,
                           admin=channel_admin)


@channel_blueprint.route("/create_channel",methods=["GET","POST"])
def create_channel():
    form = Channel_Form()
    if request.method == "POST" and form.validate_on_submit():
        new_channel = Channel()
        new_channel.channel_admin = current_user.id
        form.populate_obj(new_channel)
        new_channel.create()
        return redirect(url_for("channel.channel"))

    return render_template("channels/create_channel.html",form = form)


@channel_blueprint.route("/delete/<int:message_id>", methods=['POST'])
def delete_message(message_id):
    message_to_delete = Message.query.get_or_404(message_id)
    message_to_delete.delete()

    return redirect(url_for("channel.channel_chat",channel_id=message_to_delete.channel_id))


@channel_blueprint.route("/delete_channel/<int:channel_id>",methods=["POST"])
def delete_channel(channel_id):
    channel_to_delete = Channel.query.get_or_404(channel_id)
    channel_to_delete.delete()

    return redirect(url_for("channel.channel"))