import random
import time

from flask import Blueprint, abort, jsonify, render_template, request

from ..database.db import Sensor

# from flask_socketio import emit

# from .. import socketio

site = Blueprint('site', __name__, template_folder='templates',
                 static_folder='static')


@site.route("/api/ingess/<int:id>", methods=["POST"])
def ingest_data(id):
    sensor = Sensor.get_via_id(id)
    data = request.json

    if 'flow' not in data or 'rpm' not in data:
        abort(400)

    sensor.update_values(data['flow'], data['rpm'])
    return ('', 204)


@site.route("/api/sensor/<int:id>")
def get_sensor_data(id):
    sensor = Sensor.get_via_id(id)
    return jsonify(sensor.to_dict())


@site.route("/api/sensors")
def get_sensors_data():
    sensors = Sensor.get_all()
    data = [sensor.to_dict() for sensor in sensors]
    return jsonify(data)


@site.route('/')
def index():
    return render_template('index.html')


@site.route('/overview')
def test():
    return render_template('overview.html')
