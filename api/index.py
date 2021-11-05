from flask import Flask, request, jsonify
import requests
import lyricsgenius
import os

def get_mgmt_token():
	import http.client

	conn = http.client.HTTPSConnection("andrewemery.us.auth0.com")

	payload = "{\"client_id\":\"bBRlcj24dVatLE1Ci5Q6e7QGsyDzdJ45\",\"client_secret\":\"{}\",\"audience\":\"https://andrewemery.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}".format(os.environ['MGMT_CLIENT_SECRET'])

	headers = { 'content-type': "application/json" }

	conn.request("POST", "/oauth/token", payload, headers)

	res = conn.getresponse()
	data = res.read()
	stringData = data.decode("utf-8")
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
	artist = request.args.get('artist')
	title = request.args.get('title')
	lyrics = getGeniusLyrics(artist, title)
	data = jsonify({'lyrics' : lyrics})
	stringData = get_mgmt_token()
	return stringData
