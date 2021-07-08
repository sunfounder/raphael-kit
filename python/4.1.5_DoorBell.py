#!/usr/bin/env python3
from picamera import PiCamera
from pygame import mixer
import RPi.GPIO as GPIO
import time

camera = PiCamera()

BtnPin = 18
cameraStatus = False
musicStatus = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BtnPin, GPIO.IN, GPIO.PUD_UP)
    mixer.init()

def takePhotos(pin):
    global cameraStatus, musicStatus
    cameraStatus = True
    musicStatus = True

def main():
    global cameraStatus, musicStatus
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=takePhotos)
    while True:
        if musicStatus:
            mixer.music.load('/home/pi/raphael-kit/music/doorbell.wav')
            mixer.music.set_volume(0.7)
            mixer.music.play()
            musicStatus = False
        if cameraStatus:
            camera.start_preview(alpha=200)
            camera.start_recording('/home/pi/visitor.h264')
            print ('Have a visitor')
            time.sleep(5)
            mixer.music.stop()
            camera.stop_preview()
            camera.stop_recording()
            cameraStatus = False 

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
