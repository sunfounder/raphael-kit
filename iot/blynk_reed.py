
import BlynkLib

BLYNK_AUTH = '337A0t0PWvZrzXFp4KWTKOMUm1BPdJng' #'YourAuthToken'

# init Reed Switch
import RPi.GPIO as GPIO
ReedPin = 17
GPIO.setmode(GPIO.BCM) 
GPIO.setup(ReedPin, GPIO.IN)    # Set ReedPin's mode is input


def detect(ev=None):
    state=GPIO.input(ReedPin)
    blynk.virtual_write(4, state)

GPIO.add_event_detect(ReedPin, GPIO.BOTH, callback=detect, bouncetime=200)

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
