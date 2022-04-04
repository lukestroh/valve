"""
valve.py

Luke Strohbehn
"""

import RPi.GPIO as GPIO
import time

class Valve:
    """
    Please see README for coding challenge assumptions.
    """
    def __init__(
        self,
        sensor_closed_pin: int, # feedback sensor closed input pin
        sensor_open_pin: int, # feedback sensor open input pin
        dir_pin: int, # direction control pin
        step_pin: int # step control pin
    ):
        self.closed_pin = closed_pin
        self.open_pin = open_pin
        self.dir_pin = dir_pin
        self.step_pin = step_pin

        self.step_delay = 0.01 # (s). Determines stepper motor speed.

        GPIO.setmode(GPIO.BCM) # list pins by GPIO number and not board number.
        # Define input/output pins
        GPIO.setup(self.closed_pin, GPIO.IN)
        GPIO.setup(self.open_pin, GPIO.IN)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)

    def read(self):
        self.closed: bool = GPIO.input(self.closed_pin)
        self.open: bool = GPIO.input(self.open_pin)

    def step(self): # step the motor
        GPIO.output(self.step_pin, GPIO.HIGH)
        time.sleep(self.step_delay)
        GPIO.output(self.step_pin, GPIO.LOW)
        time.sleep(self.step_delay)

    def open_valve(self):
        self.read()
        # drive motor counterclockwise
        GPIO.output(self.dir_pin, GPIO.HIGH)
        # step until self.open == True
        while not self.open:
            self.step()
            self.read()

    def close_valve(self):
        self.read()
        # drive motor clockwise
        GPIO.output(self.dir_pin, GPIO.LOW)
        # step until self.closed == True
        while not self.closed:
            self.step()
            self.read()
