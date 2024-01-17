#!/usr/bin/env python3
from gpiozero import Button
import time

# Initialize the obstacle sensor connected to GPIO pin 17
# The sensor is configured with a pull-up resistor
obstacle_sensor = Button(17, pull_up=True)  

try:
    # Continuously monitor for obstacles
    while True:
        if obstacle_sensor.is_pressed:  # Check if the sensor is triggered
            print("Detected Barrier!")  # Print a message when an obstacle is detected
            time.sleep(1)  # Delay for 1 second to avoid repetitive messages

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) for a clean and safe exit
    pass
