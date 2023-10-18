#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

BeepPin = 27
ReedPin = 17

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BeepPin, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(ReedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(ReedPin) == 0:
            GPIO.output(BeepPin, GPIO.HIGH)	
        else:
            GPIO.output(BeepPin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(BeepPin, GPIO.HIGH)
            time.sleep(0.1)

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
