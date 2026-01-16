#!/usr/bin/env python3
import time
import os
import RPi.GPIO as GPIO
from picamera2 import Picamera2

# ----------------------------
# USER DIRECTORY
# ----------------------------
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

# ----------------------------
# GPIO SETUP
# ----------------------------
PIR_PIN = 17  # PIR motion sensor connected to GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# ----------------------------
# CAMERA SETUP
# ----------------------------
camera = Picamera2()
camera.start()

print("Motion detection started. Press Ctrl+C to exit.")

# ----------------------------
# MAIN LOOP
# ----------------------------
try:
    i = 1
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            filename = f"{user_home}/capture{i}.jpg"
            camera.capture_file(filename)
            print(f"Motion detected. Saved image #{i}: {filename}")
            time.sleep(3)
            i += 1
        else:
            print("waiting")
            time.sleep(0.5)

# ----------------------------
# KEYBOARD INTERRUPT
# ----------------------------
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting program...")

# ----------------------------
# CLEANUP
# ----------------------------
finally:
    try:
        camera.close()
    except:
        pass

    GPIO.cleanup()
    print("Program exited cleanly.")
