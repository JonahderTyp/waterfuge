import time
import RPi.GPIO as GPIO


class RpmMeter:
    pulses = 0
    last_time = time.time()

    def __init__(self, pin):
        self.pin = pin

        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.FALLING,
                              callback=self.calculate_elapsed_time_rpm)

    def calculate_elapsed_time_rpm(self, channel):
        self.pulses += 1

    def get_rpm(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        self.last_time = current_time
        rps = self.pulses / elapsed_time
        self.pulses = 0

        return rps * 60
