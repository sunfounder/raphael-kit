#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set #17 as touch switch pin, #22 as led1 pin, #27 as led2 pin
touchPin = 17
led1Pin = 22
led2Pin = 27

# Define a setup function for some setup
def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set touchPin input
	# Set ledPin output, 
	# and initial level to High(3.3v)
	GPIO.setup(touchPin, GPIO.IN)
	GPIO.setup(led1Pin, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(led2Pin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
	while True:
		# touch switch high, led1 on
		if GPIO.input(touchPin) == 1:
			print ('You touch it!')
			GPIO.output(led1Pin, GPIO.LOW)
			GPIO.output(led2Pin, GPIO.HIGH)

		# touch switch low, led2 on
		if GPIO.input(touchPin) == 0:
			GPIO.output(led2Pin, GPIO.LOW)
			GPIO.output(led1Pin, GPIO.HIGH)

		time.sleep(0.5)
# Define a destroy function for clean up everything after
# the script finished 
def destroy():
	# Turn off LED
	GPIO.output(led1Pin, GPIO.HIGH)
	GPIO.output(led2Pin, GPIO.HIGH)
	# Release resource
	GPIO.cleanup()                     

# If run this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the program 
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()	




