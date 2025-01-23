from time import sleep

from datasender.comunication import ConnectionError, DataSender
from datasender.flowmeter import FlowMeter
from datasender.rpmmeter import RpmMeter


def run(serverurl):

    # Create a FlowMeter object
    print("Setting up Flow Meter...", end="")
    flow_meter = FlowMeter(
        pin=26, liter_per_roataion=0.00225, pulses_per_rotation=1)
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

        print(f"rpm:{rpm} \t flow:{flow_rate}")

        # Send the flow rate to the server
        try:
            data_sender.sendMesurment(rpm, flow_rate)
        except ConnectionError:
            # Conection Failed, Some LED status sometime here
            print("CONNECTION FAILED")
            pass
        else:
            # Conection Successfull, Some LED status sometime here
            pass

        # Wait for 1 second
        sleep(1)
