# utils/adc.py

import spidev


def create_spi(bus: int = 0, device: int = 0, speed_hz: int = 1_000_000):
    spi = spidev.SpiDev()
    spi.open(bus, device)
    spi.max_speed_hz = speed_hz
    return spi


def read_adc(spi, channel: int) -> int:
    if channel < 0 or channel > 7:
        raise ValueError("MCP3008 channel must be between 0 and 7")

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]