import time
from tts import TTS
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

serial = spi(port=0, device=1, gpio=noop())
device = max7219(serial, rotate=1)
virtual = viewport(device, width=200, height=400)

reader = SimpleMFRC522()

tts = TTS(engine="espeak")
tts.lang('en-US')

attendance_statistics = {}

def get_time():
	time.time()
	year = str(time.strftime('%Y',time.localtime(time.time())))
	month = str(time.strftime('%m',time.localtime(time.time())))
	day = str(time.strftime('%d',time.localtime(time.time())))
	hour = str(time.strftime('%H',time.localtime(time.time())))
	minute = str(time.strftime('%M',time.localtime(time.time())))
	second = str(time.strftime('%S',time.localtime(time.time())))
	present_time = year + '.' + month + '.' + day + '.' + hour + '.' + minute + '.' + second
	present_date = year + '.' + month + '.' + day
	return present_date, present_time

def main():
    while True:
        print("Reading...Please place the card...")
        id, name = reader.read()
        print(id,name)
        greeting = name.rstrip() + ", Welcome!"
        present_date, present_time = get_time()
        attendance_statistics[name.rstrip()] = present_time
        tts.say(greeting)
        with open('attendance_sheet.' + present_date + '.csv', 'w') as f:
            [f.write('{0}  {1}\n'.format(key, value)) for key, value in attendance_statistics.items()]
        with canvas(virtual) as draw:
            text(draw, (0, 0), greeting, fill="white", font=proportional(CP437_FONT))
        for offset in range(95):
            virtual.set_position((offset,0))
            time.sleep(0.1)

def destroy():
    GPIO.cleanup()
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()


