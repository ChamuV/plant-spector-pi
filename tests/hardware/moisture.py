# tests/hardware/moisture.py

from time import sleep

from utils.adc import create_spi, read_adc
from watering.config import (
    SPI_BUS,
    SPI_DEVICE,
    ADC_CHANNEL
)


def moisture_label(value: int) -> str:
    if value > 200:
        return "DRY"
    elif value > 80:
        return "DAMP"
    else:
        return "WET"


spi = create_spi(
    bus=SPI_BUS,
    device=SPI_DEVICE
)

try:
    print("Reading moisture sensor...")
    print("Press Ctrl+C to stop.\n")

    while True:
        value = read_adc(spi, ADC_CHANNEL)

        print(
            f"CH{ADC_CHANNEL}: "
            f"{value:4d} | "
            f"{moisture_label(value)}"
        )

        sleep(1)

except KeyboardInterrupt:
    print("\nStopping moisture test")

finally:
    spi.close()