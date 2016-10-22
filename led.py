import RPi.GPIO as GPIO
import time
import os
import thread

led_one = 37
led_two = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_one, GPIO.OUT)
GPIO.setup(led_two, GPIO.OUT)

def play_music(threadName, delay):
        try:
                os.system('omxplayer -o local /home/pi/Desktop/project1/Let_It_Go_FROZEN.mp3')
        except:
                print "Music Error"
                
def play_led(threadName, delay):
        file = open('/home/pi/Desktop/project1/LetItGo.txt')
        pret = 0.0
        try:
                while True:
                        line = file.readline().strip('\n').split(',')
                        if line == ['']:
                                break
                        t = float(line[0])
                        status = bool(int(line[1]))
                        time.sleep((t - pret) / 1000)
                        GPIO.output(led_one, status)
                        GPIO.output(led_two, not status)
                        pret = t
        except KeyboardInterrupt:
                pass
try:
        thread.start_new_thread(play_music, ("Thread1", 0,))
        thread.start_new_thread(play_led, ("Thread2", 0,))
except:
        print "Error: Unable to start thread"

time.sleep(300)
GPIO.cleanup()
