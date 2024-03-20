import requests


def games_list():
	url = "https://steamgames-special-offers.p.rapidapi.com/games_list/"

	querystring = {"start":"0","count":"10","region":"US"}

	headers = {
		"X-RapidAPI-Key": "54ccf1d4e5msh2a950f20546441bp12b6acjsn7fbcbe2c6a67",
		"X-RapidAPI-Host": "steamgames-special-offers.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	response_json = response.json()

	games_list = response_json.get('games_list', [])
	return games_list


def game_name(game_id):
	all_game_name = []
	for game in game_id:
		url = "https://steamgames-special-offers.p.rapidapi.com/games_data/"

		querystring = {"app_id":f"{game}"}

		headers = {
			"X-RapidAPI-Key": "54ccf1d4e5msh2a950f20546441bp12b6acjsn7fbcbe2c6a67",
			"X-RapidAPI-Host": "steamgames-special-offers.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)
		response_json = response.json()
		print(response_json)
		name = response_json.get('title')
		all_game_name.append(name)
	return all_game_name



