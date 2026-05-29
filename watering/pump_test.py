from gpiozero import OutputDevice
from time import sleep

PUMP_PIN = 4
PUMP_SECONDS = 10

pump = OutputDevice(
    PUMP_PIN,
    active_high=True,
    initial_value=False
)

try:
    print("Pump OFF")
    pump.off()
    sleep(1)

    print(f"Pump ON for {PUMP_SECONDS} seconds")
    pump.on()
    sleep(PUMP_SECONDS)

    print("Pump OFF")
    pump.off()
    sleep(1)

finally:
    pump.off()
    print("GPIO cleanup done")