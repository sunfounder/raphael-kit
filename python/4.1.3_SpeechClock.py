import RPi.GPIO as GPIO
from tts import TTS
import time

# Initialize TTS
tts = TTS(engine="espeak")
tts.lang('en-US')

# GPIO pins
SDI = 24
RCLK = 23
SRCLK = 25

placePin = (10, 22, 27, 17)

# Seven-segment encoding
number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    for pin in placePin:
        GPIO.setup(pin, GPIO.OUT)

def clearDisplay():
    for _ in range(8):
        GPIO.output(SDI, 1)
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)

def hc595_shift(data):
    for i in range(8):
        GPIO.output(SDI, (0x80 & (data << i)))
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)

def pickDigit(digit):
    # Turn all digits off
    for pin in placePin:
        GPIO.output(pin, GPIO.LOW)
    # Turn selected digit ON
    GPIO.output(placePin[digit], GPIO.HIGH)

def loop():
    status = 0

    while True:
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min

        # Display minute (unit)
        clearDisplay()
        pickDigit(0)
        hc595_shift(number[minute % 10])

        # Display minute (tens)
        clearDisplay()
        pickDigit(1)
        hc595_shift(number[(minute // 10) % 10])

        # Display hour (unit)
        clearDisplay()
        pickDigit(2)
        hc595_shift(number[hour % 10])

        # Display hour (tens)
        clearDisplay()
        pickDigit(3)
        hc595_shift(number[(hour // 10) % 10])

        # Speak once every hour (at minute == 0)
        if minute == 0 and status == 0:
            tts.say(f'The time is now {hour} hours and {minute} minutes')
            time.sleep(3)   # Give time to finish speaking
            status = 1
        elif minute != 0:
            status = 0

        time.sleep(0.005)  # Prevent CPU overload

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()

    # ★ Welcome message at startup
    tts.say("Clock system started. Welcome!")
    time.sleep(3)

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
