from flask import Flask, request, jsonify
import http.client
import requests
import lyricsgenius
import os

def get_mgmt_token():

	conn = http.client.HTTPSConnection("")

	payload = "grant_type=client_credentials&client_id=%24%7Baccount.clientId%7D&client_secret=YOUR_CLIENT_SECRET&audience=https%3A%2F%2F%24%7Baccount.namespace%7D%2Fapi%2Fv2%2F"

	headers = { 'content-type': "application/x-www-form-urlencoded" }

	conn.request("POST", "/andrewemery.us.auth0.com/oauth/token", payload, headers)

	res = conn.getresponse()
	data = res.read()

	# stringData = data.decode("utf-8")
	stringData="test"
	return stringData

# fetch genius lyrics token
def getToken():

	data = {
	  'client_id': 'TjidTt_p0RhWw65nuJpEJH8OoqHjylagsuuOOebC8DTRjw1dgPQ1Gi2phyV1kS28',
	  'client_secret': os.environ['GENIUS_SECRET'],
	  'grant_type': 'client_credentials'
	}

	response = requests.post('https://api.genius.com/oauth/token', data=data)
	token = response.json()['access_token']
	return token

# get lyrics using genius api key and lyricsgenius library
def getGeniusLyrics(artist, title):
	token = getToken()
	genius = lyricsgenius.Genius(token)
	song = genius.search_song(title, artist)
	lyrics = song.lyrics
	return lyrics

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
	# artist = request.args.get('artist')
	# title = request.args.get('title')
	# lyrics = getGeniusLyrics(artist, title)
	# data = jsonify({'lyrics' : lyrics})
	stringData = get_mgmt_token()
	return stringData
