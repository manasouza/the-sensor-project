#!/usr/bin/env python
"""
	Detects motion and outputs a LED. 
    Credits: https://github.com/pimylifeup/motion_sensor/blob/master/motion_sensor.py

    __author__ = "gus-pimylifeup"
    __version__ = "1.0"
    __maintainer__ = "pimylifeup.com"
"""

import RPi.GPIO as GPIO
import time

pir_sensor = 11
led = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        # time in seconds
        time.sleep(0.5)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is HIGH" % pir_sensor)
            GPIO.output(led, True)
        else:
            print("GPIO pin %s is LOW" % pir_sensor)
            GPIO.output(led, False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
