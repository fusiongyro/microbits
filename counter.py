from microbit import *
import radio

radio.on()
counter = 0
while True:
    if button_a.was_pressed():
        radio.send(str(counter))
        counter = counter + 1
        display.show(Image.SURPRISED)
    elif button_b.was_pressed():
        counter = 0
        radio.send(str(counter))
        counter = counter + 1
        display.show(Image.SURPRISED)
    else:
        display.show(Image.HAPPY)

    
