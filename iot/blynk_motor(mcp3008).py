#!/usr/bin/env python3

import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import spidev
import math

BLYNK_AUTH = 'sN3E23SSENUiSzQJyPBmOkq3lSgGUGSQ'  # Replace with your own token

# GPIO pin definitions
motorPinA = 13
motorPinB = 19

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPinA, GPIO.OUT)
GPIO.setup(motorPinB, GPIO.OUT)
GPIO.output(motorPinA, GPIO.LOW)
GPIO.output(motorPinB, GPIO.LOW)

# Initialize SPI for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000  # 1 MHz

# Blynk setup
blynk = BlynkLib.Blynk(BLYNK_AUTH)
timer = BlynkTimer()

# Read from MCP3008 channel (0–7)
def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

# Convert analog reading to temperature (°C)
def getTem():
    analogVal = read_adc(0)  # CH0
    Vr = 3.3 * analogVal / 1023.0  # MCP3008 is 10-bit (0–1023), using 3.3V ref
    if Vr <= 0:
        return 0  # Prevent division by zero
    Rt = 10000.0 * (3.3 - Vr) / Vr
    tempK = 1.0 / (((math.log(Rt / 10000.0)) / 3950.0) + (1.0 / (273.15 + 25.0)))
    Cel = tempK - 273.15
    return Cel

# Send temperature to Blynk every 5 seconds
def publish_data():
    tempVal = getTem()
    string = f"{tempVal:.2f}°C"
    blynk.virtual_write(0, string)

timer.set_interval(5, publish_data)

# Motor control via Blynk V3
@blynk.on("V3")
def v3_write_handler(value):
    if int(value[0]) > 0:
        GPIO.output(motorPinA, GPIO.HIGH)
    else:
        GPIO.output(motorPinA, GPIO.LOW)

def destroy():
    GPIO.output(motorPinA, GPIO.LOW)
    GPIO.cleanup()
    spi.close()

try:
    while True:
        blynk.run()
        timer.run()
except KeyboardInterrupt:
    destroy()
