from .comunication import DataSender
from .flowmeter import FlowMeter
from .rpmmeter import RpmMeter
from .smoother import Smoother
from time import sleep


def main():
    # Create a FlowMeter object
    flow_meter = FlowMeter(
        pin=17, liter_per_roataion=450, pulses_per_rotation=1)
    rpm_meter = RpmMeter(pin=27, pulses_per_rotation=1)

    # Create a DataSender object
    data_sender = DataSender()

    while True:
        # Get the current flow rate
        flow_rate = flow_meter.get_flow()

        rpm = rpm_meter.get_rpm()

        # Send the flow rate to the server
        data_sender.sendMesurment(rpm, flow_rate)

        # Wait for 1 second
        sleep(1)
