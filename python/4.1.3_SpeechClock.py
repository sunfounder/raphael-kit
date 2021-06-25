import RPi.GPIO as GPIO
from tts import TTS
import time

tts = TTS(engine="espeak")
tts.lang('en-US')

SDI = 24
RCLK = 23
SRCLK = 18

placePin = (10, 22, 27, 17)
number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    for i in placePin:
        GPIO.setup(i, GPIO.OUT)

def clearDisplay():
    for i in range(8):
        GPIO.output(SDI, 1)
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)    

def hc595_shift(data): 
    for i in range(8):
        GPIO.output(SDI, 0x80 & (data << i))
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)

def pickDigit(digit):
    for i in placePin:
        GPIO.output(i,GPIO.LOW)
    GPIO.output(placePin[digit], GPIO.HIGH)

def loop():
    status = 0                   
    while True:
        time.localtime(time.time())
        hour = int(time.strftime('%H',time.localtime(time.time())))
        minute = int(time.strftime('%M',time.localtime(time.time())))

        clearDisplay() 
        pickDigit(0)  
        hc595_shift(number[minute % 10])
        
        clearDisplay()
        pickDigit(1)
        hc595_shift(number[minute % 100//10])

        clearDisplay()
        pickDigit(2)
        hc595_shift(number[hour % 10])

        clearDisplay()
        pickDigit(3)
        hc595_shift(number[hour % 100//10])

        if minute == 0 and status == 0:
            tts.say('The time is now ' + str(hour) + ' hours and ' + str(minute) + ' minutes')
            status = 1
        elif minute != 0:
            status = 0

def destroy():   # When "Ctrl+C" is pressed, the function is executed.
    GPIO.cleanup()

if __name__ == '__main__':  # Program starting from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()



