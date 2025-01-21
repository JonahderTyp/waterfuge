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


# Dictionary to store the data received from each server
data_store = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
}

# Route to receive data from servers (POST request)


@site.post('/data/<client_id>/')
def receive_data(client_id):
    global data_store

    client_id = str(client_id)

    if client_id not in data_store:
        print("Invalid client_id")
        return abort(404)

    data = request.json
    if 'rpm' not in data or 'flow' not in data:
        print("Missing values for rpm or flow")
        print(data)
        return jsonify({'error': 'Missing values for rpm or flow'}), 400

    rpm = float(data['rpm'])
    flow = float(data['flow'])
    timestamp = time.time()

    data_store[client_id].append(
        {'timestamp': timestamp, 'rpm': rpm, 'flow': flow})

    return jsonify({'message': 'Values stored successfully', 'client_id': client_id, 'timestamp': timestamp}), 200


@site.get('/data/<client_id>')
def display_data(client_id):
    global data_store

    current_time = time.time()
    thirty_seconds_ago = current_time - 30

    # Check if the client_id exists in the data_store
    if client_id not in data_store:
        return jsonify({'error': 'Client ID not found'}), 404

    # Filter the client's data to get values from the last 30 seconds
    client_data = data_store[client_id]
    recent_values = [
        entry for entry in client_data if thirty_seconds_ago <= entry['timestamp'] <= current_time
    ]
    return jsonify(recent_values), 200


@site.route('/')
def index():
    return render_template('index.html')


@site.route('/overview')
def test():
    return render_template('overview.html')
