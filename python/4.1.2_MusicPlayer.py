from pygame import mixer
import RPi.GPIO as GPIO
import time
import os
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')


BtnPin1 = 18
BtnPin2 = 17
BtnPin3 = 27
volume = 0.7

status = False
upPressed = False
downPressed = False
playPressed = False

def setup():
    mixer.init()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BtnPin1, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(BtnPin2, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(BtnPin3, GPIO.IN, GPIO.PUD_UP)

def clip(x,min,max):
    if x < min:
        return min
    elif x > max:
        return max
    return x

def play(pin):
    global playPressed
    playPressed = True

def volDown(pin):
    global downPressed
    downPressed = True

def volUp(pin):
    global upPressed
    upPressed = True

def main():
    global volume, status
    global downPressed, upPressed, playPressed
    mixer.music.load(f'{user_home}/raphael-kit/music/my_music.mp3')
    mixer.music.set_volume(volume)
    mixer.music.play()
    GPIO.add_event_detect(BtnPin1, GPIO.FALLING, callback=play)
    GPIO.add_event_detect(BtnPin2, GPIO.FALLING, callback=volDown)
    GPIO.add_event_detect(BtnPin3, GPIO.FALLING, callback=volUp)
    while True:
        if upPressed:
            volume = volume + 0.1
            upPressed = False
        if downPressed:
            volume = volume - 0.1
            downPressed = False
        if playPressed:
            if status:
                mixer.music.pause()
                status = not status
            else:
                mixer.music.unpause()
                status = not status
            playPressed = False
            time.sleep(0.5)
        volume = clip(volume,0.2,1)
        mixer.music.set_volume(volume)
        time.sleep(0.1)

def destroy():
	# Release resource
    GPIO.cleanup()
    mixer.music.stop()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
	    main()
	# When 'Ctrl+C' is pressed, the program 
	# destroy() will be  executed.
    except KeyboardInterrupt:
	    destroy()