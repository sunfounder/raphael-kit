#!/usr/bin/env python3
from gpiozero import LED, Button  # Import LED and Button classes from gpiozero
from time import sleep  # Import sleep function for delays

# Initialize micro switch on GPIO pin 17 with the pull-up resistor disabled
micro_switch = Button(17, pull_up=False)
# Initialize LED1 connected to GPIO pin 22
led1 = LED(22)
# Initialize LED2 connected to GPIO pin 27
led2 = LED(27)

try:
    # Continuously check the state of the micro switch and control LEDs accordingly
    while True:
        if micro_switch.is_pressed:  # If the micro switch is pressed
            print('LED1 ON')  # Print a message to the console
            led1.on()       # Turn on LED1
            led2.off()      # Turn off LED2
        else:  # If the micro switch is not pressed
            print('    LED2 ON')  # Print a message to the console
            led1.off()      # Turn off LED1
            led2.on()       # Turn on LED2

        sleep(0.5)  # Pause for 0.5 seconds before checking the switch again

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) to exit the loop gracefully
    pass
