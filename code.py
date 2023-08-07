# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: Unlicense
"""
CircuitPython Simple Example for BME280 and LC709203 Sensors
"""
import time
import board
import digitalio
from adafruit_bme280 import basic as adafruit_bme280

# Defining LED
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

# Create sensor objects, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match your location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

try:
    time_from_start = 0
    start = time.monotonic()
    with open("/temperature.txt", "a") as temp_log:
        while True:
            now = time.monotonic()
            # BME280 temperature in F
            temperature = ((bme280.temperature * 1.8) + 32)

            # BME280 humidity %
            humidity = bme280.relative_humidity

            # BME280 pressure hPa
            pressure = bme280.pressure

            # Write the temperature to the temperature.txt file every 60 seconds and update time_from_start.
            temp_log.write(
                "{}, {}, {}\n".format(temperature, humidity, time_from_start)
            )
            temp_log.flush()
            # Blink the LED on every write...
            led.value = True
            time.sleep(1)  # ...for one second.
            led.value = False

            time_from_start += 60
            time.sleep(60)


except OSError as e:  # When the filesystem is NOT writable by CircuitPython...
    delay = 0.5  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.15  # ...blink the LED every 0.15 seconds!
    while True:
        led.value = not led.value
        time.sleep(delay)
