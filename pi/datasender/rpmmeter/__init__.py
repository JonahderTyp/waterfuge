import time
from collections import deque

import RPi.GPIO as GPIO


class RpmMeter:

    def __init__(self, pin, pulses_per_rotation=1, smoothing_window=5.0):
        self.pin = pin
        self.pulses_per_rotation = pulses_per_rotation
        self.smoothing_window = smoothing_window  # Smoothing window in seconds
        self.lastTrigger = time.time()
        self.lastCall = time.time()
        self.timestamps = []

        GPIO.setmode(GPIO.BCM)
        print(f"Setting up on pin {self.pin}")
        if GPIO.event_detected(self.pin):
            print("Removed previus event detect")
            GPIO.remove_event_detect(self.pin)

        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.FALLING,
                              callback=self._sensor_triggered)

    def _sensor_triggered(self, channel):
        """
        Callback function that is triggered when the sensor detects a pulse.
        """
        if channel != self.pin:
            print("wrong channel")
            return
        current_time = time.time()
        diff = current_time - self.lastTrigger
        self.lastTrigger = current_time
        self.timestamps.append((current_time, diff))

    def get_rpm(self):
        """
        Calculate and return the current RPM based on the smoothing window.

        :return: The calculated RPM (revolutions per minute).
        """
        current_time = time.time()
        diff = current_time - self.lastCall
        self.lastCall = current_time

        # Remove timestamps older than the smoothing window
        while self.timestamps and self.timestamps[0][0] < current_time - self.smoothing_window:
            self.timestamps.pop(0)

        length = len(self.timestamps)
        rps = 0
        if length > 0:
            rps = (length/self.pulses_per_rotation)/self.smoothing_window

        rpm = rps*60

        return rpm

    def cleanup(self):
        """
        Clean up the GPIO resources when done.
        """
        GPIO.cleanup()
