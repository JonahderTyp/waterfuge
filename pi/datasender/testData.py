import json
import socket
from time import sleep

from comunication import DataSender
from configobj import ConfigObj
from flowmeter import FlowMeter
from listen import get_server_ip
from rpmmeter import RpmMeter


def main():
    config = ConfigObj("config.cfg")

    # Create a FlowMeter object
    flow_meter = FlowMeter(
        pin=17, liter_per_roataion=450, pulses_per_rotation=1)
    rpm_meter = RpmMeter(pin=27, pulses_per_rotation=1)

    # Create a DataSender object
    data_sender = DataSender(
        f"http://{get_server_ip().get('ip', '0.0.0.0')}:8080/upload/{config.get('system_id')}/")

    # Send some data
    while True:
        data_sender.sendMesurment(100, 10)
        sleep(1)
        data_sender.sendMesurment(200, 20)
        sleep(1)
        data_sender.sendMesurment(300, 30)
        sleep(1)
        data_sender.sendMesurment(400, 40)
        sleep(1)
        data_sender.sendMesurment(500, 50)
        sleep(1)


if __name__ == "__main__":
    main()
