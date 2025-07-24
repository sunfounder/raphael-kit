
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import spidev
import time

# Define GPIO pin for joystick button (SW pin)
BTN_PIN = 22

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use internal pull-up

# Initialize SPI communication with MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, CE0
spi.max_speed_hz = 1000000  # 1 MHz

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
        # Read X and Y values from MCP3008 channels 1 and 2
        x_val = read_adc(1)  # Joystick VRX connected to CH1
        y_val = read_adc(2)  # Joystick VRY connected to CH2

        # Read the state of the joystick button (SW)
        Btn_val = GPIO.input(BTN_PIN)  # 0 = pressed, 1 = released

        # Print the read values
        print('X: %d  Y: %d  Btn: %d' % (x_val, y_val, Btn_val))

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    spi.close()
    GPIO.cleanup()
