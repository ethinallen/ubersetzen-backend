from flask import Flask
from flask import request
import requests
import lyricsgenius
import os

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
	return lyrics
