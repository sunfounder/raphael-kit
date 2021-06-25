from pygame import mixer

mixer.init()

def main():
    mixer.music.load('/home/pi/mozart-kit-for-raspberry-pi/music/my_music.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
	    pass# Don't do anything.

def destroy():
    mixer.music.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()