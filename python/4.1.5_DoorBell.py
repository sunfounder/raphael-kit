#!/usr/bin/env python3
from picamera import PiCamera
from pygame import mixer
import RPi.GPIO as GPIO
import time
import os
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

camera = PiCamera()

BtnPin = 18
status = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BtnPin, GPIO.IN, GPIO.PUD_UP)
    mixer.init()

def takePhotos(pin):
    global status
    status = True

def main():
    global status
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=takePhotos)
    while True:
        if status:
            mixer.music.load(f'{user_home}/raphael-kit/music/doorbell.wav')
            mixer.music.set_volume(0.7)
            mixer.music.play()
            camera.start_preview(alpha=200)
            camera.start_recording(f'{user_home}/visitor.h264')
            print ('Have a visitor')
            time.sleep(5)
            mixer.music.stop()
            camera.stop_preview()
            camera.stop_recording()
            status = False 

def destroy():
    GPIO.cleanup()
    mixer.music.stop()
    camera.stop_preview()
    camera.stop_recording()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
