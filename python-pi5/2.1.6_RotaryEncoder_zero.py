#!/usr/bin/env python3
from gpiozero import RotaryEncoder, Button
from time import sleep

# Initialize the rotary encoder and button
encoder = RotaryEncoder(a=17, b=18)  # Rotary Encoder connected to GPIO pins 17 (CLK) and 18 (DT)
button = Button(27)                  # Button connected to GPIO pin 27

global_counter = 0  # Track the rotary encoder's position

def rotary_change():
    """ Update the global counter based on the rotary encoder's rotation. """
    global global_counter
    global_counter += encoder.steps  # Adjust counter based on encoder steps
    encoder.steps = 0  # Reset encoder steps after updating counter
    print('Global Counter =', global_counter)  # Display current counter value

def reset_counter():
    """ Reset the global counter to zero when the button is pressed. """
    global global_counter
    global_counter = 0  # Reset the counter
    print('Counter reset')  # Indicate counter reset

# Assign the reset_counter function to button press event
button.when_pressed = reset_counter

try:
    # Monitor rotary encoder continuously and process changes
    while True:
        rotary_change()  # Handle rotary encoder changes
        sleep(0.1)  # Short delay to reduce CPU load

except KeyboardInterrupt:
    # Gracefully handle a keyboard interrupt (Ctrl+C)
    pass
