from flask import Flask
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
from flask import Flask
import lyricsgenius
import os

def getToken():
	data = {
	  'client_id': 'TjidTt_p0RhWw65nuJpEJH8OoqHjylagsuuOOebC8DTRjw1dgPQ1Gi2phyV1kS28',
	  'client_secret': os.environ['GENIUS_SECRET'],
	  'grant_type': 'client_credentials'
	}

	response = requests.post('https://api.genius.com/oauth/token', data=data)
	token = response.text
	return token

# def getGeniusLyrics(title, artist):
# 	response =

app = Flask(__name__)

@app.route('/api')
def api():
	token = getToken()
	return token
