#!/usr/bin/env python3    
    
from picamera import PiCamera

camera = PiCamera()

def setup():
    camera.start_preview(alpha=200)

def main():
    camera.capture('/home/pi/my_photo.jpg')
    while True:
        pass    

def destroy():
    camera.stop_preview()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()