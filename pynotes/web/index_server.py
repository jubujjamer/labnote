##########################################################
# File client.py
# Author:
# Date:
#
##########################################################

import base64
import json
import socket
import os

from flask import Flask, Response, render_template, request

FOLDER = os.path.abspath(os.path.dirname(__file__))


def create_server(fdates=None):
    app = Flask("Labnote", template_folder=os.path.join(FOLDER, 'templates'),
                       static_folder=os.path.join(FOLDER, 'static'))
    @app.route("/")
    def init():
        return Response("Testing")

    @app.route("/index")
    def index():
        return render_template('index.html', dates=fdates)

    @app.route('/calendar')
    def calendar():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', 'summary.json')
        data = json.load(open(json_url))


        return render_template('calendar.html',
                               data=data)

    return app
