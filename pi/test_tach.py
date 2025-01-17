from datasender.rpmmeter import RpmMeter
from RPi.GPIO import cleanup
from time import sleep

try:
    rpm_meter = RpmMeter(pin=25, pulses_per_rotation=2)
    
    while True:
        print(rpm_meter.get_rpm())
        sleep(1)
finally:
    cleanup()
