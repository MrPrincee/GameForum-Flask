from flask import render_template, Blueprint, redirect, url_for, request

from src.views.offer.api import games_list, game_name

offer_blueprint = Blueprint("offer", __name__)


@offer_blueprint.route("/offers")
def offer():
    all_games = games_list()
    all_games_name = game_name(all_games)
    test_games = [381210,2446550,1551360,2427700,582010,1621690,961200]
    test_name = ["Dead_by_Daylight","STAR_WARS_Battlefront_Classic_Collection","Forza_Horizon_5","Backpack_Battles","Monster_Hunter_World","Core_Keeper","Predecessor"]
    print(all_games)
    print(all_games_name)
    return render_template("offers/offers.html", games_list=test_games, game_name=test_name)

