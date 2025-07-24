#!/usr/bin/env python3

import spidev
import time
from gpiozero import PWMLED

# Initialize PWM LED on GPIO22
led = PWMLED(22)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CS0 (CE0)
spi.max_speed_hz = 1000000

def read_adc(channel):
    """
    Read analog value from MCP3008
    :param channel: ADC channel (0-7)
    :return: 10-bit integer (0-1023)
    """
    if channel < 0 or channel > 7:
        return -1
    # MCP3008 protocol
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) | adc[2]
    return value

def MAP(x, in_min, in_max, out_min, out_max):
    """
    Map a value from one range to another
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    while True:
        # Read from MCP3008 channel 0
        res = read_adc(0)
        print('res = %d' % res)

        # Map 0–1023 to 0–100%
        R_val = MAP(res, 0, 1023, 0, 100)

        # Set LED brightness
        led.value = R_val / 100.0

        time.sleep(0.2)

except KeyboardInterrupt:
    led.value = 0  # Turn off the LED
