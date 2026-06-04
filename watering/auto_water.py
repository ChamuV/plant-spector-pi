# watering/auto_water.py

import spidev
from gpiozero import OutputDevice
from time import sleep
from datetime import datetime

# MCP3008 settings
SPI_BUS = 0
SPI_DEVICE = 0
ADC_CHANNEL = 0

# Pump settings
PUMP_PIN = 4
PUMP_SECONDS = 2

# From calibration:
# Air: ~1023
# Dry soil: ~256-271
# Damp soil: ~128-143
# Wet soil: ~0-48
DRY_THRESHOLD = 200


def read_adc(channel: int) -> int:
    if channel < 0 or channel > 7:
        raise ValueError("MCP3008 channel must be between 0 and 7")

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) + adc[2]
    return value


def should_water(value: int) -> bool:
    return value > DRY_THRESHOLD


def run_pump(seconds: int) -> None:
    print(f"Pump ON for {seconds} seconds")
    pump.on()
    sleep(seconds)
    pump.off()
    print("Pump OFF")


spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 1_000_000

pump = OutputDevice(
    PUMP_PIN,
    active_high=True,
    initial_value=False
)

try:
    moisture_value = read_adc(ADC_CHANNEL)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{now}] Moisture reading CH{ADC_CHANNEL}: {moisture_value}")

    if should_water(moisture_value):
        print(f"Soil is dry: {moisture_value} > {DRY_THRESHOLD}")
        run_pump(PUMP_SECONDS)
    else:
        print(f"Soil is wet enough: {moisture_value} <= {DRY_THRESHOLD}")
        pump.off()

finally:
    pump.off()
    spi.close()
    print("Cleanup done")