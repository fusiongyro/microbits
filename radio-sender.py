# Add your Python code here. E.g.
from microbit import *
import radio

toggle = True
radio.on()
while True:
    if button_a.was_pressed():
        radio.send('HELLO')
        display.show(Image.HEART)
    elif button_b.was_pressed():
        radio.send('GOODBYE')
        display.show(Image.HEART)
    else:
        display.show(Image.DIAMOND)
