
#!/usr/bin/env python3

import spidev
import time
import RPi.GPIO as GPIO

# GPIO pin for PWM output
PWM_PIN = 22

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Initialize PWM on GPIO22 at 1000Hz
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)  # Start with 0% duty cycle

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000

def read_adc(channel):
    """
    Read analog value from MCP3008
    :param channel: ADC channel (0-7)
    :return: 10-bit integer (0-1023)
    """
    if channel < 0 or channel > 7:
        return -1
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
        # Read analog value from CH0
        res = read_adc(0)
        print('res = %d' % res)

        # Convert to 0–100% duty cycle
        duty_cycle = MAP(res, 0, 1023, 0, 100)

        # Update PWM duty cycle
        pwm.ChangeDutyCycle(duty_cycle)

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
    spi.close()
