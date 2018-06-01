from microbit import *
import random

blank = Image("00000:00000:00000:00000:00000")  # blank

faces = [Image("00000:00000:00900:00000:00000"),  # 1
         Image("90000:00000:00000:00000:00009"),  # 2
         Image("90000:00000:00900:00000:00009"),  # 3
         Image("90009:00000:00000:00000:90009"),  # 4
         Image("90009:00000:00900:00000:90009"),  # 5
         Image("90009:00000:90009:00000:90009")]  # 6

last_roll = blank
while True:
    if accelerometer.was_gesture("shake"):
        last_roll = random.choice(faces)
        display.show([faces[0],faces[3],faces[2],faces[1],faces[4],faces[3],faces[5],faces[0]], delay=100)
    display.show(last_roll)
