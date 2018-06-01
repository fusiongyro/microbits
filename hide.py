# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
# radio.config(power=7)

display.scroll('HIDE ME!')
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed() or button_b.was_pressed():
        display.scroll('YOU FOUND ME!')
        display.show(Image.SURPRISE)
    else:
        display.show(Image.TARGET)
        radio.send('A')
    sleep(1000)
