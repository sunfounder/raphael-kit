#!/usr/bin/env python3
from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
import time
import os

# Retrieve the current user's login name and home directory
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

# Initialize the camera
camera = Picamera2()
camera.start()

# Initialize the motion sensor on GPIO pin 17
pir = MotionSensor(17)

try:
    i = 1  # Initialize the image count
    while True:
        if pir.motion_detected:
            # Capture an image when motion is detected and save it with a unique number
            camera.capture_file(f'{user_home}/capture%s.jpg' % i)
            print('The number is %s' % i)  # Print the image count
            time.sleep(3)  # Wait for 3 seconds before next detection
            i += 1  # Increment the image count
        else:
            print('waiting')  # Print 'waiting' when no motion is detected
            time.sleep(0.5)  # Check for motion every 0.5 seconds

except KeyboardInterrupt:
    # Stop the camera and turn off the LED if a KeyboardInterrupt occurs
    camera.stop_preview()
    pass
