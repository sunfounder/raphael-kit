#!/usr/bin/env python3

import LCD1602
from gpiozero import LED, Buzzer, Button
import spidev
import time
import math

# Initialize joystick button, buzzer, and LED
Joy_BtnPin = Button(22)  # GPIO22, Pin15
buzzPin = Buzzer(23)     # GPIO23, Pin16
ledPin = LED(24)         # GPIO24, Pin18

# Set initial upper temperature threshold
upperTem = 40

# Initialize SPI for MCP3008 (Bus 0, CE0 -> GPIO8 / Pin24)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000  # 1 MHz

# Initialize LCD (I2C address 0x27, backlight on)
LCD1602.init(0x27, 1)

def read_adc(channel):
    """
    Read analog value from MCP3008 (0–7)
    """
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 0x03) << 8) | adc[2]
    return value

def get_joystick_value():
    """
    Reads the joystick values and returns a change value based on the joystick's position.
    """
    x_val = read_adc(1)
    y_val = read_adc(2)
    if x_val > 800:
        return 1
    elif x_val < 200:
        return -1
    elif y_val > 800:
        return -10
    elif y_val < 200:
        return 10
    else:
        return 0

def upper_tem_setting():
    """
    Adjusts and displays the upper temperature threshold on the LCD.
    """
    global upperTem
    LCD1602.write(0, 0, 'Upper Adjust: ')
    change = int(get_joystick_value())
    upperTem += change
    strUpperTem = str(upperTem)
    LCD1602.write(0, 1, strUpperTem)
    LCD1602.write(len(strUpperTem), 1, '              ')
    time.sleep(0.1)

def temperature():
    """
    Reads the current temperature from the sensor and returns it in Celsius.
    """
    analogVal = read_adc(0)
    Vr = 3.3 * analogVal / 1023.0  # Voltage across the fixed resistor
    if Vr == 0:
        return 0  # Prevent division by zero
    Rt = 10000.0 * (3.3 - Vr) / Vr  # Adjusted formula: thermistor voltage is (3.3 - Vr)
    temp = 1 / (((math.log(Rt / 10000.0)) / 3950.0) + (1 / (273.15 + 25.0)))
    Cel = temp - 273.15
    return round(Cel, 2)

def monitoring_temp():
    """
    Monitors and displays the current temperature and upper temperature threshold.
    Activates buzzer and LED if the temperature exceeds the upper limit.
    """
    global upperTem
    Cel = temperature()
    LCD1602.write(0, 0, 'Temp: ')
    LCD1602.write(0, 1, 'Upper: ')
    LCD1602.write(6, 0, str(Cel))
    LCD1602.write(7, 1, str(upperTem))
    time.sleep(0.1)
    if Cel >= upperTem:
        buzzPin.on()
        ledPin.on()
    else:
        buzzPin.off()
        ledPin.off()

# Main execution loop
try:
    lastState = 1
    stage = 0
    while True:
        currentState = Joy_BtnPin.value
        if currentState == 1 and lastState == 0:
            stage = (stage + 1) % 2
            time.sleep(0.1)
            LCD1602.clear()
        lastState = currentState
        if stage == 1:
            upper_tem_setting()
        else:
            monitoring_temp()
except KeyboardInterrupt:
    LCD1602.clear()
    spi.close()
