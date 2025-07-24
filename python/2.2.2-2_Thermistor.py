
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spidev
import time
import math
import RPi.GPIO as GPIO

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Initialize SPI for MCP3008 (Bus 0, CE0)
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, Device 0 (CE0)
spi.max_speed_hz = 1000000  # 1 MHz

def read_adc(channel):
    """
    Read analog value from MCP3008 channel (0–7)
    """
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

try:
    while True:
        # Read analog value from CH0 of MCP3008
        analogVal = read_adc(0)

        # Convert to voltage (assuming 3.3V reference)
        Vr = 3.3 * analogVal / 1023.0

        # Calculate thermistor resistance (R2 in voltage divider is 10kΩ)
        Rt = 10000.0 * Vr / (3.3 - Vr)

        # Steinhart–Hart calculation
        tempK = 1.0 / (((math.log(Rt / 10000.0)) / 3950.0) + (1.0 / (273.15 + 25.0)))

        # Convert to Celsius and Fahrenheit
        Cel = tempK - 273.15
        Fah = Cel * 1.8 + 32

        # Print the result
        print('Celsius: %.2f °C  Fahrenheit: %.2f °F' % (Cel, Fah))

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    spi.close()
    GPIO.cleanup()
