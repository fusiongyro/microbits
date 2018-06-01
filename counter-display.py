from microbit import *
import radio

def draw_counter(counter):
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9 if counter > 5*x+y else 0)

radio.on()
count = 0
while True:
    message = radio.receive()
    if message:
        count = int(message)
    draw_counter(count)
    
