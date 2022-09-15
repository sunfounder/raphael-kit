import BlynkLib
import RPi.GPIO as GPIO 

BLYNK_AUTH = '337A0t0PWvZrzXFp4KWTKOMUm1BPdJng' #'YourAuthToken'

# Init Device
ledPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
ledPWM = GPIO.PWM(ledPin, 2000)
ledPWM.start(0)
led_switch = False
led_brightness = 0
ledPWM.ChangeDutyCycle(led_brightness)

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler
@blynk.on("V3")
def v3_write_handler(value):
    global led_switch
    if int(value[0]) is not 0:
        led_switch = True
    else:
        led_switch = False

# Register virtual pin handler
@blynk.on("V2")
def v2_write_handler(value):
    global led_brightness
    led_brightness = int(value[0])

# KeyboardInterrupt
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

try:
    while True:
        blynk.run()
        if led_switch is True:
            ledPWM.ChangeDutyCycle(led_brightness)
        else:
            ledPWM.ChangeDutyCycle(0)
except KeyboardInterrupt:
    destroy()