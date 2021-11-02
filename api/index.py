from flask import Flask
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
from flask import Flask




app = Flask(__name__)

@app.route('/api')
def api():
    return "dingle dangle"
