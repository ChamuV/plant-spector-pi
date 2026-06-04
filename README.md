# PlantSpector Pi

Plants need regular watering and sunlight to stay green, healthy, and happy. While outdoor plants can often rely on rain and natural sunlight, indoor plants depend almost entirely on us for their care. Unfortunately, it is surprisingly easy to forget about them, even when you have plenty of free time.

In my attempt to keep plants indoors while still being slightly lazy about remembering when they were last watered, I decided to automate the process. Rather than relying on memory, I wanted a system that could monitor a plant's condition and water it only when needed.

Automatic irrigation systems are nothing new, and Raspberry Pi plant waterers are one of the most common hobby electronics projects online. This project takes inspiration from many of those existing systems. However, rather than simply reproducing an existing design, my goal is to gradually adapt and extend it into a platform that provides more of the conditions plants experience outdoors. Over time, I hope to build an ecosystem that can manage not only moisture, but also lighting, temperature, cooling, monitoring, and data collection, one step at a time.

The current version uses a capacitive soil moisture sensor connected through an MCP3008 ADC to a Raspberry Pi. Moisture levels are checked automatically, and when the soil becomes too dry, a MOSFET-controlled pump delivers water to the plant. Readings and watering events are logged for later analysis, and the entire process runs automatically using cron scheduling.

---

## Current Features

- Capacitive soil moisture sensing
- MCP3008 ADC over SPI
- Automatic watering logic
- MOSFET-controlled water pump
- CSV moisture logging
- Cron-based scheduling
- Modular Python project structure

---

## Hardware Used

### Core Components

- Raspberry Pi 5
- MCP3008 10-bit ADC
- Capacitive Soil Moisture Sensor v2.0
- MOSFET switch module
- Mini water pump
- Breadboard and jumper wires
- Water reservoir and tubing

---

## Project Structure

```text
plant-spector-pi/
??? watering/
?   ??? auto_water.py
?   ??? config.py
?   ??? __init__.py
?
??? utils/
?   ??? adc.py
?   ??? pump.py
?   ??? logger.py
?   ??? __init__.py
?
??? deployment/
?   ??? cron_schedule.txt
?
??? logs/
?
??? README.md
```

---

## Moisture Calibration

Approximate readings observed during testing:

| Condition | Reading |
|-----------|---------|
| Air | ~1023 |
| Dry Soil | ~250 |
| Damp Soil | ~130 |
| Water | ~0-50 |

Current watering threshold:

```python
DRY_THRESHOLD = 200
```

---

## Running Manually

```bash
python3 -m watering.auto_water
```

---

## Scheduled Watering

The system is currently configured to check soil moisture every four hours using cron.

Example schedule:

```cron
0 */4 * * * cd /path/to/plant-spector-pi && /usr/bin/python3 -m watering.auto_water
```

---

## Future Ideas

Planned future extensions include:

- Raspberry Pi Pico migration for lower power consumption
- Grow-light control and scheduling
- Temperature and humidity monitoring
- Automated image capture using a camera
- Time-lapse generation and plant growth tracking
- Vegetation indices and NDVI-style analysis
- Models for predicting watering requirements

---

## Current Status

**Version:** v0.1 ? Autonomous Watering System

---

## License
S
This project is released under the MIT License.


