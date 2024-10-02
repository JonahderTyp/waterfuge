from flask import Blueprint, jsonify, render_template, request

# from flask_socketio import emit

# from .. import socketio

site = Blueprint('site', __name__, template_folder='templates',
                 static_folder='static')

# Dictionary to store the data received from each server
data_store = {
    "server_1": None,
    "server_2": None,
    "server_3": None,
    "server_4": None
}

# Route to receive data from servers (POST request)


@site.route('/receive_data/<server_id>', methods=['POST'])
def receive_data(server_id):
    if server_id not in data_store:
        return jsonify({"error": "Invalid server ID"}), 400

    # Assume data is sent in JSON format
    received_data = request.get_json()
    if not received_data or 'value' not in received_data:
        return jsonify({"error": "Invalid data format"}), 400

    # Store the value from the server
    data_store[server_id] = received_data['value']

    return jsonify({"message": f"Data received from {server_id}"}), 200

# Route to display the current values from all servers


@site.route('/')
def display_data():
    return jsonify(data_store)
