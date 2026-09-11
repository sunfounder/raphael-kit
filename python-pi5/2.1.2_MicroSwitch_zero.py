#!/usr/bin/env python3

from gpiozero import LED, Button
from time import sleep

# Initialize the micro switch (LOW when pressed)
micro_switch = Button(17, pull_up=None, active_state=False, bounce_time=0.05)

# Initialize the LEDs
red_led = LED(22)
yellow_led = LED(27)

try:
    while True:
        if micro_switch.is_pressed:
            print("YELLOW LED ON")
            red_led.off()
            yellow_led.on()
        else:
            print("RED LED ON")
            red_led.on()
            yellow_led.off()

        sleep(0.1)

except KeyboardInterrupt:
    # Turn off both LEDs
    red_led.off()
    yellow_led.off()
