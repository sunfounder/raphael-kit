import BlynkLib
import RPi.GPIO as GPIO 
from BlynkTimer import BlynkTimer
import ADC0834
import math

BLYNK_AUTH = '337A0t0PWvZrzXFp4KWTKOMUm1BPdJng' #'YourAuthToken'

# Init Device
motorPinA = 13
motorPinB = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPinA, GPIO.OUT)
GPIO.setup(motorPinB, GPIO.OUT)
GPIO.output(motorPinA, GPIO.LOW)
GPIO.output(motorPinB, GPIO.LOW)
ADC0834.setup()


# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()

# Get Temperature
def getTem():
    analogVal = ADC0834.getResult()
    Vr = 5 * float(analogVal) / 255
    Rt = 10000 * Vr / (5 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    #Fah = Cel * 1.8 + 32
    return Cel

# Will Print Every 5 Seconds
def publish_data():
    tempVal=getTem()
    string=str("%.2f"%tempVal) +"°C"
    #print(string)
    blynk.virtual_write(0, string)

# Add Timers
timer.set_interval(5, publish_data)

# Register virtual pin handler
@blynk.on("V3")
def v3_write_handler(value):
    #print('Value: {}'.format(value[0]))
    if int(value[0])>0:
        GPIO.output(motorPinA, GPIO.HIGH)
    else:
        GPIO.output(motorPinA, GPIO.LOW)

def destroy():
    GPIO.output(motorPinA, GPIO.LOW)
    GPIO.cleanup()

try:
    while True:
        blynk.run()
        timer.run()
except KeyboardInterrupt:
    destroy()