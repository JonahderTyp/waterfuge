from flask import Flask

# from flask_socketio import SocketIO

# socketio = SocketIO()


def create_app():
    app = Flask(__name__)

    from .site import site
    app.register_blueprint(site)

    # socketio.init_app(app)

    return app
