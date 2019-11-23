from microbit import *
import radio

radio.on()

while True:
    state = radio.receive()
    if state in ['face up', 'face down']:
        print(state)
