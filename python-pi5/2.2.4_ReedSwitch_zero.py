#!/usr/bin/env python3
from gpiozero import LED, Button

# Initialize the reed switch and LEDs using GPIO Zero
reed_switch = Button(17, pull_up=True)  # Reed switch on GPIO 17, using an internal pull-up resistor
green_led = LED(27)                     # Green LED connected to GPIO pin 27
red_led = LED(22)                       # Red LED connected to GPIO pin 22

def update_leds():
    """
    Update the state of the LEDs based on the reed switch.
    Turns the red LED on and green LED off when the reed switch is pressed, and vice versa.
    """
    if reed_switch.is_pressed:
        green_led.off()          # Turn off the green LED
        red_led.on()             # Turn on the red LED
    else:
        green_led.on()           # Turn on the green LED
        red_led.off()            # Turn off the red LED

try:
    green_led.on()               # Turn on the green LED at the start
    while True:
        # Set the callback functions for reed switch state changes
        reed_switch.when_pressed = update_leds   # Callback when the switch is pressed
        reed_switch.when_released = update_leds  # Callback when the switch is released

except KeyboardInterrupt:
    # Clean up resources and exit on Ctrl+C
    green_led.off()
    red_led.off()
    pass
