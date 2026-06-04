# watering/moisture_test.py

import spidev
from time import sleep

SPI_BUS = 0
SPI_DEVICE = 0
ADC_CHANNEL = 0


def read_adc(channel: int) -> int:
    if channel < 0 or channel > 7:
        raise ValueError("MCP3008 channel must be between 0 and 7")

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) + adc[2]
    return value


def moisture_label(value: int) -> str:
    if value > 200:
        return "DRY"
    elif value > 80:
        return "DAMP"
    else:
        return "WET"


spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 1_000_000

try:
    print("Reading moisture sensor on MCP3008 CH0...")
    print("Press Ctrl+C to stop.\n")

    while True:
        value = read_adc(ADC_CHANNEL)
        label = moisture_label(value)
        print(f"CH{ADC_CHANNEL}: {value:4d}  |  {label}")
        sleep(1)

except KeyboardInterrupt:
    print("\nStopping moisture test")

finally:
    spi.close()