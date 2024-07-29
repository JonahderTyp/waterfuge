import time
import RPi.GPIO as GPIO
from collections import deque


class FlowMeter:
    def __init__(self, pin, pulses_per_litre, window_size=5):
        self.pin = pin
        self.pulses_per_litre = pulses_per_litre
        self.window_size = window_size

        self.flow_readings = deque()
        self.last_time = time.time()
        self.flow = 0

        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.FALLING,
                              callback=self.calculate_elapsed_time_flow)

    def calculate_elapsed_time_flow(self, channel):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        self.last_time = current_time
        pulsesPerMinute = 60 / elapsed_time  #
        current_flow = pulsesPerMinute / self.pulses_per_litre  # L/min

        # Add current flow reading to the deque
        self.flow_readings.append((current_time, current_flow))

        # Remove outdated readings
        while self.flow_readings and self.flow_readings[0][0] < current_time - self.window_size:
            self.flow_readings.popleft()

        # Compute the average flow over the last window_size seconds
        total_flow = sum(flow for _, flow in self.flow_readings)
        self.flow = total_flow / len(self.flow_readings)

    def get_flow(self):
        return self.flow
