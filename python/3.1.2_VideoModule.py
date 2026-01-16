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

camera = Picamera2()

# --- PREVIEW CONFIGURATION ---
preview_config = camera.create_preview_configuration(
    main={"size": (800, 600), "format": "XRGB8888"}
)

camera.configure(preview_config)
camera.start_preview(Preview.QTGL)
camera.start()

try:
    # --- VIDEO RECORDING CONFIG ---
    video_conf = camera.create_video_configuration(
        main={"size": (800, 600)},
        controls={"FrameRate": 40},
        buffer_count=12
    )

    camera.configure(video_conf)

    encoder = H264Encoder(bitrate=10_000_000)
    output = FfmpegOutput(f"{user_home}/my_video.mp4")

    camera.start_recording(encoder, output)
    time.sleep(10)
    camera.stop_recording()

except KeyboardInterrupt:
    pass

finally:
    camera.stop_preview()
    camera.close()
