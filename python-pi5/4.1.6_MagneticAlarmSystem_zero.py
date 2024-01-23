#!/usr/bin/env python3
from gpiozero import Buzzer, Button
import time

# Initialize the buzzer on GPIO pin 27
buzzer = Buzzer(27)
# Initialize the reed switch on GPIO pin 17 with pull-up resistor enabled
reed_switch = Button(17, pull_up=True)

try:
    while True:
        # Check if the reed switch is pressed
        if reed_switch.is_pressed:
            # Turn off the buzzer if reed switch is pressed
            buzzer.off()
        else:
            # If reed switch is not pressed, beep the buzzer
            buzzer.on()
            time.sleep(0.1)  # Buzzer on for 0.1 seconds
            buzzer.off()
            time.sleep(0.1)  # Buzzer off for 0.1 seconds

except KeyboardInterrupt:
    # Turn off the buzzer when the program is interrupted (e.g., keyboard interrupt)
    buzzer.off()
    pass
