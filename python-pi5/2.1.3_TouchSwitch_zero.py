#!/usr/bin/env python3
from gpiozero import LED, Button  # Import LED and Button classes from gpiozero
from time import sleep  # Import sleep for delay

# Initialize touch sensor (Button) on GPIO pin 17, pull-up resistor disabled
touch_sensor = Button(17, pull_up=False)  # Suitable for sensors that pull the pin low when pressed

# Initialize LED1 and LED2 connected to GPIO pins 22 and 27 respectively
led1 = LED(22)  # LED1 connected to GPIO pin 22
led2 = LED(27)  # LED2 connected to GPIO pin 27

try:
    # Continuously monitor the state of the touch sensor and control LEDs accordingly
    while True:
        if touch_sensor.is_pressed:  # Check if the touch sensor is pressed
            print('You touch it!')  # Output message indicating sensor activation
            led1.off()  # Turn off LED1
            led2.on()   # Turn on LED2
        else:  # If the sensor is not pressed
            led1.on()   # Turn on LED1
            led2.off()  # Turn off LED2

        sleep(0.5)  # Pause for 0.5 seconds before rechecking the sensor state

except KeyboardInterrupt:
    # Handle a keyboard interrupt (Ctrl+C) for a clean exit from the loop
    pass
