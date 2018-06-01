from microbit import *
import radio

enabled = True
radio.on()
radio.config(power=1)
while True:
    if button_a.was_pressed():
        enabled = not enabled
        if enabled: radio.on()
        else: radio.off()
    
    if enabled:
        radio.send('A')
        display.show(Image.HOUSE)
    else:
        display.show(Image.NO)
        
    sleep(1000)
