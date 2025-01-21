
from .db import Sensor


def seed_database():
    Sensor.create_sensor("Team 1")
    Sensor.create_sensor("Team 2")
    Sensor.create_sensor("Team 3")
    Sensor.create_sensor("Team 4")
