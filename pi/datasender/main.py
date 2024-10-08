from time import sleep

from configobj import ConfigObj

from .comunication import DataSender
from .flowmeter import FlowMeter
from .listen import get_server_ip
from .rpmmeter import RpmMeter


def main(config: ConfigObj):

    # Create a FlowMeter object
    flow_meter = FlowMeter(
        pin=17, liter_per_roataion=450, pulses_per_rotation=1)
    rpm_meter = RpmMeter(pin=27, pulses_per_rotation=1)

    # Create a DataSender object
    data_sender = DataSender(
        f"http://{get_server_ip().get('ip', '0.0.0.0')}:8080/upload/{config.get('system_id')}/")

    while True:
        # Get the current flow rate
        flow_rate = flow_meter.get_flow()

        rpm = rpm_meter.get_rpm()

        # Send the flow rate to the server
        data_sender.sendMesurment(rpm, flow_rate)

        # Wait for 1 second
        sleep(1)
