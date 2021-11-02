from flask import Flask
from http.server import BaseHTTPRequestHandler
from urllib import parse

from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home Page Route</h1>'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    return "dingle dangle"
