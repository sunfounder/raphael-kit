#!/usr/bin/env python3
import spidev
import time
from gpiozero import PWMLED

# Initialize a PWM LED on GPIO pin 22
led = PWMLED(22)

# Initialize SPI communication (Bus 0, CE0 -> GPIO8)
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CS0
spi.max_speed_hz = 1000000  # 1 MHz

# Function to read from MCP3008 channel (0–7)
def read_adc(channel):
    """
    Read analog value from MCP3008 (0–1023)
    """
    if channel < 0 or channel > 7:
        return -1
    # MCP3008 protocol: Start bit, Single-ended mode, Channel (3 bits), filler
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((r[1] & 3) << 8) | r[2]
    return value

# Define a function for mapping values from one range to another
def MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Main loop for reading ADC value and controlling LED brightness
def loop():
    while True:
        # Read analog value from channel 0 of MCP3008
        analogVal = read_adc(0)
        print('value = %d' % analogVal)

        # Map 0–1023 to PWM range 0.0–1.0
        led.value = analogVal / 1023.0

        # Wait for 0.2 seconds
        time.sleep(0.2)

# Run the main loop and handle KeyboardInterrupt for graceful shutdown
try:
    loop()
except KeyboardInterrupt:
    led.value = 0  # Turn off LED before exiting
