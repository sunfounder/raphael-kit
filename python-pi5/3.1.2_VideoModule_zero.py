#!/usr/bin/env python3

import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
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
    # Configure preview size and format
    preview_config.size = (800, 600)
    preview_config.format = 'XRGB8888'
    # Start the camera preview in QTGL mode
    camera.start_preview(Preview.QTGL)

    # Define video configuration with size, frame rate, and buffer count
    conf = {'size': (800, 600)}
    controls = {'FrameRate': 40}
    config = camera.create_video_configuration(main=conf, controls=controls, buffer_count=12)
    # Create a video encoder with a specified bitrate
    encoder = H264Encoder(bitrate=10000000)
    # Define output file for the video
    output = FfmpegOutput(f'{user_home}/my_video.mp4')
    # Configure and start recording
    camera.configure(config)
    camera.start_recording(encoder, output)
    # Record for 10 seconds
    time.sleep(10)
    # Stop the recording
    camera.stop_recording()

except KeyboardInterrupt:
    # Stop the camera preview if a KeyboardInterrupt (e.g., Ctrl+C) occurs
    camera.stop_preview()
    pass
