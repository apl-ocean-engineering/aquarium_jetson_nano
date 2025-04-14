# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import analogio

# Create sensor object, using the board's default I2C bus.
i2c = board.STEMMA_I2C()  # uses board.SCL and board.SDA

# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


adc = [analogio.AnalogIn(board.A2), analogio.AnalogIn(board.A3)]

# OR create sensor object, using the board's default SPI bus.
# import digitalio
# spi = board.SPI()
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:

    # Hand-format this as JSON ...
    #  end=''" means "no endline"
    print("{", end='')
    print("\"temperature\": %0.1f," % bme280.temperature, end='')
    print("\"humidity\": %0.1f," % bme280.relative_humidity, end='')
    print("\"pressure\": %0.1f," % bme280.pressure, end='')
    print("\"altitude\": %0.2f," % bme280.altitude, end='')

    adc_v = [
        channel.value / 65535 * channel.reference_voltage for channel in adc
    ]
    print("\"leak\": { \"leak0_voltage\": %.2f, \"leak1_voltage\": %.2f}" % (adc_v[0], adc_v[1]), end='')

    print("}")

    time.sleep(2)
