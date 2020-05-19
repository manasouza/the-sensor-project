#!/usr/local/bin/python
"""
https://github.com/pimylifeup/Light_Sensor/blob/master/light_sensor.py
"""

import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def get_rc_time():
    #Catch when script is interupted, cleanup correctly
    try:
        # Main loop
        while True:
            rc_time_value = rc_time(pin_to_circuit)
            print(rc_time_value)            
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()