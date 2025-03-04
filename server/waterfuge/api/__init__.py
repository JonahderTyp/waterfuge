from flask import Blueprint, abort, jsonify, request

from ..database.db import Sensor

api_site = Blueprint('api', __name__, url_prefix='/api')


@api_site.route("/ingess/<int:id>", methods=["POST"])
def ingest_data(id):
    sensor = Sensor.get_via_id(id)
    data = request.json

    if 'flow' not in data or 'rpm' not in data:
        abort(400)

    sensor.update_values(data['flow'], data['rpm'])
    return ('', 204)


@api_site.route("/sensor/<int:id>")
def get_sensor_data(id):
    sensor = Sensor.get_via_id(id)
    return jsonify(sensor.to_dict())


@api_site.route("/sensors")
def get_sensors_data():
    sensors = Sensor.get_all()
    data = [sensor.to_dict() for sensor in sensors]
    return jsonify(data)
