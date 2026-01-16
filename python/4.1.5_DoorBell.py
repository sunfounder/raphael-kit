#!/usr/bin/env python3
import time
import os
import RPi.GPIO as GPIO
from pygame import mixer
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

# --------------------------------------------------
# USER DIRECTORY
# --------------------------------------------------
user = os.getlogin()
user_home = os.path.expanduser(f"~{user}")

# --------------------------------------------------
# CAMERA SETUP (Picamera2)
# --------------------------------------------------
camera = Picamera2()

# Create a video configuration WITHOUT the deprecated "video=" argument
video_config = camera.create_video_configuration(
    main={"size": (1280, 720), "format": "XBGR8888"}
)
camera.configure(video_config)

# Create H264 encoder (10 Mbps is good quality for doorbell)
encoder = H264Encoder(bitrate=10_000_000)

# --------------------------------------------------
# GPIO SETUP
# --------------------------------------------------
BtnPin = 18
status = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    mixer.init()

def button_pressed(pin):
    """Button callback"""
    global status
    status = True

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------
def main():
    global status
    GPIO.add_event_detect(BtnPin, GPIO.FALLING,
                          callback=button_pressed, bouncetime=250)

    print("Doorbell system running... Press the button to record.")

    while True:
        if status:
            print("Visitor detected!")

            # Play doorbell sound
            mixer.music.load(f"{user_home}/raphael-kit/music/doorbell.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()

            # Use QTGL preview
            camera.start_preview(Preview.QTGL)

            # Output file
            output_path = f"{user_home}/visitor.mp4"
            output = FfmpegOutput(output_path)

            # Start recording
            camera.start_recording(encoder, output)
            print(f"Recording video to {output_path}")

            time.sleep(5)  # Record for 5 seconds

            # Stop everything
            mixer.music.stop()
            camera.stop_recording()
            camera.stop_preview()

            print("Recording finished.\n")

            status = False

        time.sleep(0.05)

# --------------------------------------------------
# CLEAN EXIT
# --------------------------------------------------
def destroy():
    print("\nExiting...")

    mixer.quit()
    GPIO.cleanup()
    camera.close()

    print("Program exited cleanly.")

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
