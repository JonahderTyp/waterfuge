from flask import Blueprint, request, jsonify, render_template
from flask_socketio import emit
from .. import socketio

site = Blueprint('site', __name__, template_folder='templates',
                 static_folder='static')

data = []


@site.route('/data', methods=['POST'])
def receive_data():
    global data
    content = request.json
    rpm = content['rpm']
    flow = content['flow']
    data.append({'rpm': rpm, 'flow': flow})
    socketio.emit('new_data', {'rpm': rpm, 'flow': flow})
    return jsonify(success=True)


@site.route('/')
def index():
    return render_template('index.html')
