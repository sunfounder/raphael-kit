#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

clkPin = 17    # CLK Pin
dtPin = 18    # DT Pin
swPin = 27    # Button Pin

globalCounter = 0

flag = 0
Last_dt_Status = 0
Current_dt_Status = 0

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(clkPin, GPIO.IN)    # input mode
	GPIO.setup(dtPin, GPIO.IN)
	GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rotaryDeal():
	global flag
	global Last_dt_Status
	global Current_dt_Status
	global globalCounter
	Last_dt_Status = GPIO.input(dtPin)
	while(not GPIO.input(clkPin)):
		Current_dt_Status = GPIO.input(dtPin)
		flag = 1
	if flag == 1:
		flag = 0
		if (Last_dt_Status == 0) and (Current_dt_Status == 1):
			globalCounter = globalCounter - 1
		if (Last_dt_Status == 1) and (Current_dt_Status == 0):
			globalCounter = globalCounter + 1

def swISR(channel):
	global globalCounter
	globalCounter = 0

def loop():
	global globalCounter
	tmp = 0	# Rotary Temperary

	GPIO.add_event_detect(swPin, GPIO.FALLING, callback=swISR)
	while True:
		rotaryDeal()
		if tmp != globalCounter:
			print ('globalCounter = %d' % globalCounter)
			tmp = globalCounter

def destroy():
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

