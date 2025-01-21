from time import sleep

from datasender.comunication import DataSender

from datasender.flowmeter import FlowMeter
from datasender.rpmmeter import RpmMeter


def run(serverurl):

    # Create a FlowMeter object
    print("Setting up Flow Meter...", end="")
    flow_meter = FlowMeter(
        pin=17, liter_per_roataion=450, pulses_per_rotation=1)
    print("Done")
    
    print("Setting up RPM Meter...", end="")
    rpm_meter = RpmMeter(pin=25, pulses_per_rotation=1)
    print("Done")

    # Create a DataSender object
    data_sender = DataSender(serverurl)

    while True:
        # Get the current flow rate
        flow_rate = flow_meter.get_flow()
        
        rpm = rpm_meter.get_rpm()

        # Send the flow rate to the server
        data_sender.sendMesurment(rpm, flow_rate)

        # Wait for 1 second
        sleep(1)
