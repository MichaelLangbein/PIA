from flask import Flask
import pywps
from pywps import Service
from service import MyProcess



app = Flask(__name__)
wpsService = Service([MyProcess()])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return wpsService