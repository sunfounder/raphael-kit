#!/usr/bin/env python3

import RPi.GPIO as GPIO
import spidev
import time
import math

# Pin configuration
BTN_PIN = 22            # Button GPIO (physical pin 15)
MOTOR_IN1 = 5           # Motor forward
MOTOR_IN2 = 6           # Motor backward
MOTOR_EN = 13           # PWM enable pin

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(MOTOR_IN1, GPIO.OUT)
GPIO.setup(MOTOR_IN2, GPIO.OUT)
GPIO.setup(MOTOR_EN, GPIO.OUT)

# PWM setup for motor speed control
pwm = GPIO.PWM(MOTOR_EN, 1000)  # 1kHz frequency
pwm.start(0)

# Initialize SPI for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000  # 1 MHz

# Global variables
level = 0
currentTemp = 0
markTemp = 0

def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

def temperature():
    analogVal = read_adc(0)
    Vr = 3.3 * analogVal / 1023.0
    Rt = 10000.0 * Vr / (3.3 - Vr)
    tempK = 1.0 / (((math.log(Rt / 10000.0)) / 3950.0) + (1.0 / (273.15 + 25.0)))
    Cel = tempK - 273.15
    return Cel

def motor_run(level):
    if level == 0:
        GPIO.output(MOTOR_IN1, GPIO.LOW)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        pwm.ChangeDutyCycle(0)
        return 0
    if level >= 4:
        level = 4
    GPIO.output(MOTOR_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(level * 25)  # Map level (1–4) to 25%–100%
    return level

def changeLevel(channel):
    global level, currentTemp, markTemp
    print("Button pressed")
    level = (level + 1) % 5
    markTemp = currentTemp

# Add event detection for button press
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=changeLevel, bouncetime=300)

def main():
    global level, currentTemp, markTemp
    markTemp = temperature()
    while True:
        currentTemp = temperature()
        if level != 0:
            if currentTemp - markTemp <= -2:
                level -= 1
                markTemp = currentTemp
            elif currentTemp - markTemp >= 2:
                if level < 4:
                    level += 1
                markTemp = currentTemp
        level = motor_run(level)
        time.sleep(0.2)

try:
    main()
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
    spi.close()

