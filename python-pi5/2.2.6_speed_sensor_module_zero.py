#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause

# Initialize GPIO pins for the speed sensor and LEDs using GPIO Zero library
speed_sensor = Button(17, pull_up=False)  # Speed sensor connected to GPIO pin 17 without pull-up
green_led = LED(27)                      # Green LED connected to GPIO pin 27
red_led = LED(22)                        # Red LED connected to GPIO pin 22

def update_leds():
    """
    Update the state of LEDs based on the speed sensor.
    - If the sensor is pressed (triggered), the red LED is turned on and a message is printed.
    - If the sensor is released (not triggered), the green LED is turned on.
    """
    if speed_sensor.is_pressed:
        green_led.off()  # Turn off green LED
        red_led.on()     # Turn on red LED
        print('Light was blocked')  # Print message indicating sensor is triggered
    else:
        green_led.on()   # Turn on green LED
        red_led.off()    # Turn off red LED

try:
    # Main loop to continuously check sensor state
    while True:
        # Update LEDs based on sensor state changes
        speed_sensor.when_pressed = update_leds   # Update LEDs when sensor is pressed
        speed_sensor.when_released = update_leds  # Update LEDs when sensor is released

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) for a graceful script termination
    pass

