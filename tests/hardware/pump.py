# tests/hardware/pump.py

from utils.pump import create_pump, run_pump
from watering.config import (
    PUMP_PIN,
    PUMP_SECONDS
)

pump = create_pump(PUMP_PIN)

try:
    print(f"Pump ON for {PUMP_SECONDS} seconds")

    run_pump(
        pump,
        PUMP_SECONDS
    )

    print("Pump OFF")

finally:
    pump.off()

    print("Cleanup done")