#!/usr/bin/env python3

from gpiozero import Button
import spidev
import time

# Initialize the button connected to GPIO pin 22 (joystick SW pin)
BtnPin = Button(22)

# Initialize SPI communication with MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device CE0
spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz

def read_adc(channel):
    """
    Reads analog value from the specified MCP3008 channel (0–7)
    :param channel: ADC channel number (0–7)
    :return: 10-bit integer value (0–1023)
    """
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

try:
    # Main loop to read and print joystick values and button state
    while True:
        # Read X and Y values from MCP3008 channels 0 and 1
        x_val = read_adc(0)  # Joystick VRX connected to CH0
        y_val = read_adc(1)  # Joystick VRY connected to CH1

        # Read the state of the joystick button (SW)
        Btn_val = BtnPin.value  # 0 = pressed, 1 = released

        # Print the read values
        print('X: %d  Y: %d  Btn: %d' % (x_val, y_val, Btn_val))

        # Wait 0.2 seconds before the next reading
        time.sleep(0.2)

# Gracefully handle Ctrl+C interruption
except KeyboardInterrupt:
    spi.close()
