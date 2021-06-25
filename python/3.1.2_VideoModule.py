#!/usr/bin/env python3

from picamera import PiCamera

camera = PiCamera()

def setup():
	camera.start_preview(alpha=200)  # Make the camera preview see-through by setting an alpha level from 0 to 255

def main():
    camera.start_recording('/home/pi/my_video.h264')
    while True:
        pass    

def destroy():
	camera.stop_recording()
	camera.stop_preview()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()