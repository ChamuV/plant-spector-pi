# utils/pump.py

from gpiozero import OutputDevice
from time import sleep


def create_pump(pin: int):
    return OutputDevice(pin, active_high=True, initial_value=False)


def run_pump(pump, seconds: int):
    pump.on()
    sleep(seconds)
    pump.off()