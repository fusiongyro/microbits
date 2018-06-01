from microbit import *

while True:
  if accelerometer.current_gesture() == "freefall":
    display.show(Image.HAPPY)
  else:
    display.show(Image.ANGRY)
