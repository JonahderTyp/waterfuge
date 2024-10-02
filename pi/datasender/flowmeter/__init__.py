import time
import RPi.GPIO as GPIO
from ..rpmmeter import RpmMeter


class FlowMeter:
    def __init__(self, pin, liter_per_roataion, pulses_per_rotation=1):
        self.liter_per_roataion = liter_per_roataion
        self.rpm_meter = RpmMeter(
            pin=pin, pulses_per_rotation=pulses_per_rotation)

    def get_flow(self):
        return self.rpm_meter.get_rpm() / self.liter_per_roataion
