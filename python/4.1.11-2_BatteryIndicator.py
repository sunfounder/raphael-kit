
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import spidev
import time

# GPIO pins connected to 10 LEDs, ordered from left to right
led_pins = [25, 12, 16, 20, 21, 5, 6, 13, 19, 26]  # BCM numbering

# GPIO setup
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000  # 1 MHz

# Read value from MCP3008 channel (returns 0–1023)
def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((r[1] & 0x03) << 8) | r[2]
    return value

# Light up LED bar graph according to value (0–10 levels)
def led_bar_graph(level):
    for i, pin in enumerate(led_pins):
        if i < level:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

# Main loop
try:
    while True:
        analog_val = read_adc(0)  # Read from MCP3008 channel 0
        level = int(analog_val * 10 / 1023)  # Scale to 0–10
        led_bar_graph(level)
        print(f"ADC: {analog_val}, Level: {level}")
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    spi.close()
