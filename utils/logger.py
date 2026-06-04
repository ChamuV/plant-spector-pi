# utils/logger.py

from pathlib import Path
from datetime import datetime
import csv


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def log_csv(
    filename: str,
    headers: list[str],
    row: list
) -> None:
    """
    Generic CSV logger.

    Creates the file and writes headers if it does not exist.
    Appends a new row otherwise.
    """

    file_path = LOG_DIR / filename

    file_exists = file_path.exists()

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(headers)

        writer.writerow(row)


def log_moisture(
    channel: int,
    moisture: int,
    pump_on: bool,
    duration_seconds: int
) -> None:

    log_csv(
        filename="moisture.csv",
        headers=[
            "timestamp",
            "channel",
            "moisture",
            "pump_on",
            "duration_seconds"
        ],
        row=[
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            channel,
            moisture,
            int(pump_on),
            duration_seconds
        ]
    )