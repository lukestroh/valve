"""
valve.py

Luke Strohbehn

Project written under the assumption of controlling our valve with a RasPi. This script also assumes an intermediate stepper motor control board that supplies power and controls the required coils and receives step and direction inputs from the RasPi.
"""
import RPi.GPIO as GPIO
import time

class Valve:
    """
    Detection zone provided by https://www.ifm.com/de/en/product/IN5327?tab=details
    has an output function of 2x normally open. Assuming there are two circuits, one detecting a "closed" state and the other an "open" state.

    Valve is a double-acting actuator, so we need to drive the motor in two directions:
     https://us.misumi-ec.com/vona2/detail/221000099654/?HissuCode=C-UTE-50A&gclid=CjwKCAjwuYWSBhByEiwAKd_n_qlhjHMMPqnV8edrhrl9CkPO6bRHT5zkvve7IKfm-bHgQNKih050PhoCGrcQAvD_BwE&curSearch=%7b%22field%22%3a%22%40search%22%2c%22seriesCode%22%3a%22221000099654%22%2c%22innerCode%22%3a%22%22%2c%22sort%22%3a1%2c%22specSortFlag%22%3a0%2c%22allSpecFlag%22%3a0%2c%22page%22%3a1%2c%22pageSize%22%3a%2260%22%2c%2200000030969%22%3a%22k%22%2c%22jp000032588%22%3a%22mig00000000053035%22%2c%22jp000032596%22%3a%22mig00000000053031%22%2c%22jp000032600%22%3a%22mig00000000053032%22%7d&Tab=codeList

    Open direction is assumed to be counterclockwise and logic HIGH, close as clockwise and logic LOW.
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
