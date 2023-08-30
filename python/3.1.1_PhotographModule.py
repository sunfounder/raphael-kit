#!/usr/bin/env python3    
    
from picamera import PiCamera
import os
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')


camera = PiCamera()

def setup():
    camera.start_preview(alpha=200)

def main():
    camera.capture(f'{user_home}/my_photo.jpg')
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