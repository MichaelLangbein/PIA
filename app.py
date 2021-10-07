from flask import Flask, send_from_directory
from pywps import Service
from service import MyProcess



app = Flask(__name__)
wpsService = Service([MyProcess()], 'serverconfig.cfg')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return wpsService


# @app.route('/outputs/<fileName>')
# def serveFiles(fileName):
#     return send_from_directory('outputs', fileName)
