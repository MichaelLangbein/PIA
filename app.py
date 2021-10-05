from flask import Flask
import pywps
from pywps import Service



app = Flask(__name__)
# service = Service([myService], ['pywps.cfg'])
wpsService = Service([])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return wpsService