# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
radio.config(queue=1)

while True:
    mesg = radio.receive_full()
    if mesg:
        _, rssi, _ = mesg
        distance = 10 ** (rssi/20)
        display.scroll('{:5.2f}'.format(distance))
    sleep(1000)
