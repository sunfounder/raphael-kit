from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
import time

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, rotate=1)
virtual = viewport(device, width=200, height=400)

def displayRectangle():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")

def displayLetter():
    with canvas(device) as draw:
        text(draw, (0, 0), "A", fill="white", font=proportional(CP437_FONT))

def scrollToDisplayText():
    with canvas(virtual) as draw:
        text(draw, (0, 0), "Hello, Nice to meet you!", fill="white", font=proportional(CP437_FONT))

    for offset in range(150):
        virtual.set_position((offset,0))
        time.sleep(0.1)

def main():
    while True:
        displayRectangle()
        time.sleep(2)
        displayLetter()
        time.sleep(2)
        scrollToDisplayText()

def destroy():
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()