import time
import RPi.GPIO as GPIO
from collections import deque

import time
import RPi.GPIO as GPIO
from collections import deque

class RpmMeter:

    def __init__(self, pin, pulses_per_rotation=1, smoothing_window=5.0):
        self.pin = pin
        self.pulses_per_rotation = pulses_per_rotation
        self.smoothing_window = smoothing_window  # Smoothing window in seconds
        self.timestamps = deque()  # Stores timestamps of sensor triggers

        GPIO.setmode(GPIO.BCM)
        print(f"Setting up on pin {self.pin}")
        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.FALLING,
                              callback=self._sensor_triggered)

    def _sensor_triggered(self, channel):
        """
        Callback function that is triggered when the sensor detects a pulse.
        """
        current_time = time.time()
        self.timestamps.append(current_time)

        # Remove timestamps older than the smoothing window
        while self.timestamps and self.timestamps[0] < current_time - self.smoothing_window:
            self.timestamps.popleft()

    def get_rpm(self):
        """
        Calculate and return the current RPM based on the smoothing window.

        :return: The calculated RPM (revolutions per minute).
        """
        current_time = time.time()

        # Remove timestamps older than the smoothing window
        while self.timestamps and self.timestamps[0] < current_time - self.smoothing_window:
            self.timestamps.popleft()

        # Calculate the number of revolutions
        num_revolutions = len(self.timestamps) / self.pulses_per_rotation

        # Calculate the time span covered by the current timestamps
        if len(self.timestamps) > 1:
            time_span = self.timestamps[-1] - self.timestamps[0]
        elif self.timestamps:
            time_span = current_time - self.timestamps[0]
        else:
            time_span = 0

        # Calculate RPM
        if time_span > 0:
            rpm = (num_revolutions / time_span) * 60  # Convert to revolutions per minute
        else:
            rpm = 0

        return rpm

    def cleanup(self):
        """
        Clean up the GPIO resources when done.
        """
        GPIO.cleanup()
