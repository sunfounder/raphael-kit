#!/usr/bin/env python3

from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import os
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')


camera = PiCamera()

LedPin = 17 # Set GPIO17 as LED pin
BtnPin = 18 # Set GPIO18 as button pin

status = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BtnPin, GPIO.IN)
    camera.start_preview(alpha=200)

def takePhotos(pin):
    global status
    status = True

def main():
    global status
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=takePhotos)
    while True:
        if status:
            for i in range(5):
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(0.1)
            camera.capture(f'{user_home}/my_photo.jpg')
            print ('Take a photo!')          
            status = False
        else:
            GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(1)

def destroy():
    camera.stop_preview()
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		main()
	except KeyboardInterrupt:
		destroy()