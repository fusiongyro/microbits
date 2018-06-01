from microbit import *
import radio

def draw_counter(counter):
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9 if counter > 5*x+y else 0)

radio.on()
strength = 0
while True:
    if button_a.was_pressed(): strength = 0
    response = radio.receive_full()
    if response:
        strength = (response[1] / -4) - 10
    draw_counter(strength)
    sleep(10)
