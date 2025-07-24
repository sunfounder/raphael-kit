
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import spidev
import time

# GPIO pin for PWM LED
PWM_PIN = 22

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Initialize PWM (frequency = 1000Hz)
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)  # Start with 0% duty cycle

# Initialize SPI (MCP3008 on Bus 0, CE0)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000  # 1 MHz

# Function to read MCP3008 ADC value
def read_adc(channel):
    """
    Read analog value from MCP3008 (channel 0–7)
    Returns: 10-bit value (0–1023)
    """
    if channel < 0 or channel > 7:
        return -1
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((r[1] & 3) << 8) | r[2]
    return value

# Main loop to read ADC and set PWM brightness
try:
    while True:
        analogVal = read_adc(0)
        print(f"value = {analogVal}")

        # Scale ADC value (0–1023) to duty cycle (0–100)
        duty_cycle = analogVal * 100 / 1023
        pwm.ChangeDutyCycle(duty_cycle)

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
    spi.close()

