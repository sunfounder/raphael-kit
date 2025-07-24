#!/usr/bin/env python3

from gpiozero import Motor, Button
from time import sleep
import spidev
import math

# Initialize SPI for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0 (GPIO8 / physical pin 24)
spi.max_speed_hz = 1000000  # 1 MHz

# Initialize GPIO pins for the button and motor control
BtnPin = Button(22)  # GPIO22 (physical pin 15)
motor = Motor(forward=5, backward=6, enable=13)  # GPIO5, GPIO6, GPIO13

# Initialize variables to track the motor speed level and temperatures
level = 0
currentTemp = 0
markTemp = 0

def read_adc(channel):
    """
    Reads analog value from MCP3008 channel (0–7).
    """
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

def temperature():
    """
    Reads and calculates the current temperature from the sensor.
    Returns:
        float: The current temperature in Celsius.
    """
    analogVal = read_adc(0)  # Assuming thermistor connected to CH0
    Vr = 3.3 * analogVal / 1023.0  # For 3.3V system
    Rt = 10000.0 * Vr / (3.3 - Vr)
    temp = 1 / (((math.log(Rt / 10000.0)) / 3950.0) + (1 / (273.15 + 25.0)))
    Cel = temp - 273.15
    return Cel

def motor_run(level):
    """
    Adjusts the motor speed based on the specified level.
    Args:
        level (int): Desired motor speed level.
    Returns:
        int: Adjusted motor speed level.
    """
    if level == 0:
        motor.stop()
        return 0
    if level >= 4:
        level = 4
    motor.forward(speed=float(level / 4))
    return level

def changeLevel():
    """
    Changes the motor speed level when the button is pressed and updates the reference temperature.
    """
    global level, currentTemp, markTemp
    print("Button pressed")
    level = (level + 1) % 5
    markTemp = currentTemp

# Bind the button press event to changeLevel function
BtnPin.when_pressed = changeLevel

def main():
    """
    Main function to continuously monitor and respond to temperature changes.
    """
    global level, currentTemp, markTemp
    markTemp = temperature()
    while True:
        currentTemp = temperature()
        if level != 0:
            if currentTemp - markTemp <= -2:
                level -= 1
                markTemp = currentTemp
            elif currentTemp - markTemp >= 2:
                if level < 4:
                    level += 1
                markTemp = currentTemp
        level = motor_run(level)
        sleep(0.2)

# Run the main function and handle KeyboardInterrupt
try:
    main()
except KeyboardInterrupt:
    motor.stop()
    spi.close()
