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
from subprocess import call


from flask import Flask, Response, render_template, request, send_from_directory, redirect, url_for

import pynotes

FOLDER = os.path.abspath(os.path.dirname(__file__))


def create_server(fdates=None, day_dict=None, dt=None):
    app = Flask("Labnote", template_folder=os.path.join(FOLDER, 'templates'),
                       static_folder=os.path.join(FOLDER, 'static'))
    @app.route("/")
    def init():
        return Response("Testing")

    @app.route("/index")
    def index():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', 'summary.json')
        data = json.load(open(json_url))
        return render_template('index.html', dates=fdates, day_dict=day_dict, dt=dt)

    @app.route("/fast_reference")
    def fast_reference():
        return render_template('fast_reference.html')

    @app.route('/<year>-<month>-<day>')
    def show_day_page(year, month, day):
        date_str = "%s-%s-%s" % (year, month, day)
        date = dt.datetime.strptime(date_str, "%Y-%m-%d")
        path = pynotes.pynotes._get_date_path(date)
        return send_from_directory(path, date_str+'.html')

    @app.route('/folder/<year>-<month>-<day>')
    def open_day_folder(year, month, day):
        date_str = "%s-%s-%s" % (year, month, day)
        date = dt.datetime.strptime(date_str, "%Y-%m-%d")
        path = pynotes.pynotes._get_date_path(date)
        call(['nautilus', '--browser', path])
        return redirect(url_for('index'))

    @app.route('/inventory')
    def inventory():
        path = pynotes.pynotes.get_inventory_path()
        call(['xdg-open', path])
        return redirect(url_for('index'))

    @app.route('/calendar')
    def calendar():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(FOLDER, 'static', 'summary.json')
        data = json.load(open(json_url))
        return render_template('calendar.html',
                               data=data)

    return app
