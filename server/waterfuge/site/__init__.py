import random
import time

from flask import Blueprint, abort, jsonify, render_template, request

from ..database.db import Sensor

# from flask_socketio import emit

# from .. import socketio

site = Blueprint('site', __name__, template_folder='templates',
                 static_folder='static')

# Set the dark variable based on url param ?dark=true


@site.context_processor
def inject_dark():
    dark = request.args.get('dark', "False").lower() in ["true", "1"]
    return dict(dark=dark)


@site.route('/')
def index():
    return render_template('index.html')


@site.route('/overview')
def overview():
    return render_template('overview.html')
