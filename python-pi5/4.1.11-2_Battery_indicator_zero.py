#!/usr/bin/env python3
from gpiozero import LED
import spidev
import time

# List of GPIO pins to which LEDs are connected
ledPins = [25, 12, 16, 20, 21, 5, 6, 13, 19, 26]
# Initialize LED objects for each pin in the list
leds = [LED(pin) for pin in ledPins]

# Setup SPI for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)              # Open SPI bus 0, device (CE0)
spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz

def read_adc(channel=0):
    """
    Reads analog value from MCP3008 channel (default CH0).
    Returns a 10-bit value .
    """
    if channel < 0 or channel > 7:
        return -1
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((r[1] & 0x03) << 8) | r[2]
    return value

def LedBarGraph(value):
    # Turn off all LEDs
    for i in range(10):
        leds[i].off()
    # Turn on LEDs up to the specified value
    for i in range(min(value, 10)):
        leds[i].on()

try:
    # Main loop to continuously update LED bar graph
    while True:
        analogVal = read_adc(0)  # Read from CH0
        LedBarGraph(int(analogVal / 102.4)) 
        time.sleep(0.1)
except KeyboardInterrupt:
    # Turn off all LEDs when program is interrupted
    for i in range(10):
        leds[i].off()
    spi.close()
