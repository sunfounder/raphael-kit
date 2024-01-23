#!/usr/bin/env python3    

from picamera2 import Picamera2, Preview
import os

# Get the current user's login name
user = os.getlogin()
# Get the path to the user's home directory
user_home = os.path.expanduser(f'~{user}')

# Create a Picamera2 instance
camera = Picamera2()
# Retrieve the default preview configuration
preview_config = camera.preview_configuration

try:
    # Set preview size and format
    preview_config.size = (800, 600)
    preview_config.format = 'XRGB8888'  
    # Start the camera preview in QTGL mode
    camera.start_preview(Preview.QTGL)
    # Start the camera
    camera.start()
    # Capture and save a photo to the user's home directory
    camera.capture_file(f'{user_home}/my_photo.jpg')

except KeyboardInterrupt:
    # Stop the camera preview if a KeyboardInterrupt (e.g., Ctrl+C) occurs
    camera.stop_preview()
    pass
