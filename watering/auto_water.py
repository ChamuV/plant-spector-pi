# watering/auto_water.py

from datetime import datetime

from utils.adc import create_spi, read_adc
from utils.pump import create_pump, run_pump
from utils.logger import log_measurement

from watering.config import (
    SPI_BUS,
    SPI_DEVICE,
    ADC_CHANNEL,
    PUMP_PIN,
    PUMP_SECONDS,
    DRY_THRESHOLD,
)


def should_water(moisture_value: int) -> bool:
    return moisture_value > DRY_THRESHOLD


def main() -> None:

    spi = create_spi(
        bus=SPI_BUS,
        device=SPI_DEVICE
    )

    pump = create_pump(PUMP_PIN)

    try:
        moisture_value = read_adc(
            spi,
            ADC_CHANNEL
        )

        now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(
            f"[{now}] "
            f"Moisture reading CH{ADC_CHANNEL}: "
            f"{moisture_value}"
        )

        if should_water(moisture_value):

            print(
                f"Soil is dry: "
                f"{moisture_value} > {DRY_THRESHOLD}"
            )

            run_pump(
                pump,
                PUMP_SECONDS
            )

            print(
                f"Pump ran for "
                f"{PUMP_SECONDS} seconds"
            )

            log_measurement(
                moisture=moisture_value,
                pump_on=True,
                duration=PUMP_SECONDS
            )

        else:

            print(
                f"Soil is wet enough: "
                f"{moisture_value} <= {DRY_THRESHOLD}"
            )

            pump.off()

            log_measurement(
                moisture=moisture_value,
                pump_on=False,
                duration=0
            )

    finally:

        pump.off()
        spi.close()

        print("Cleanup done")


if __name__ == "__main__":
    main()