# utils/logger.py

from pathlib import Path
from datetime import datetime
import csv

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

CSV_FILE = LOG_DIR / "watering.csv"


def log_measurement(
    moisture: int,
    pump_on: bool,
    duration: int
) -> None:

    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "moisture",
                "pump_on",
                "duration_seconds"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            moisture,
            int(pump_on),
            duration
        ])