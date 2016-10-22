import mp3play
import time

clip = mp3play.load("Let It Go-FROZEN.mp3")
clip.play()
time.sleep(100)
clip.stop()
