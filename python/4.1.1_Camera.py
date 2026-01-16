#!/usr/bin/env python3
import time
import os
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview

# ----------------------------
# GPIO SETUP
# ----------------------------

BUTTON_PIN = 18  # The push button is connected to GPIO18
LED_PIN = 17     # The LED is connected to GPIO17

GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering

# The button uses a 10K pull-up resistor externally.
# When released → HIGH, when pressed → LOW.
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED is an output (HIGH → ON, LOW → OFF)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED is OFF at startup

# ----------------------------
# USER DIRECTORY SETUP
# ----------------------------

# Get the current logged-in username
user = os.getlogin()

# Build the path to the user's home directory (ex: /home/pi)
user_home = os.path.expanduser(f"~{user}")

# ----------------------------
# CAMERA SETUP
# ----------------------------

# Create a Picamera2 object
camera = Picamera2()

# Create a preview configuration:
# main → the main camera stream
# size → resolution 800x600
# format → display format used by the preview window
preview_config = camera.create_preview_configuration(
    main={"size": (800, 600), "format": "XRGB8888"}
)

# Apply the configuration to the camera
camera.configure(preview_config)

# Start the preview window using QTGL (GPU-accelerated)
camera.start_preview(Preview.QTGL)

# Start the camera hardware
camera.start()

print("Ready! Press the button to take a photo...")

# ----------------------------
# MAIN LOOP
# ----------------------------
try:
    while True:
        # Check if button is pressed (LOW means pressed)
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Button pressed! Taking photo...")

            # Flash LED 3 times to warn before taking the photo
            for _ in range(3):
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.1)

            # Build a unique filename using current date and time
            # Example: /home/pi/my_photo_20251201_143522.jpg
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(user_home, f"my_photo_{timestamp}.jpg")

            # Capture the image
            camera.capture_file(filename)

            print(f"Photo saved to: {filename}")

            # Turn LED ON briefly to confirm capture
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_PIN, GPIO.LOW)

            # Debounce delay to prevent repeated triggers
            time.sleep(0.3)

        # Small delay to reduce CPU usage
        time.sleep(0.01)

# ----------------------------
# CLEAN EXIT WHEN CTRL+C IS PRESSED
# ----------------------------
except KeyboardInterrupt:
    print("\nCtrl+C received, exiting...")

# ----------------------------
# CLEANUP SECTION
# ----------------------------
finally:
    # Safely try to stop the camera preview
    try:
        camera.stop_preview()
    except:
        pass  # Ignore errors if preview wasn't running

    # Safely close the camera device
    try:
        camera.close()
    except:
        pass

    # Reset GPIO pins to a safe state
    GPIO.cleanup()

    print("Program exited cleanly.")
