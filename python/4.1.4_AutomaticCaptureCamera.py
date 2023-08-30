#!/usr/bin/env python3

from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import os
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')


camera = PiCamera()

pirPin = 17    # the pir connect to pin17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pirPin, GPIO.IN)
    camera.start_preview(alpha=200)

def main():
    i = 1
    while True:
        pirVal = GPIO.input(pirPin)
        if pirVal==GPIO.HIGH:
            camera.capture(f'{user_home}/capture%s.jpg' % i)
            print('The number is %s' % i)
            time.sleep(3)
            i = i + 1

def destroy():
    GPIO.cleanup()
    camera.stop_preview()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()