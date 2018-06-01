from microbit import *

def draw_counter(counter):
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9 if counter > 5*x+y else 0)

counter = 0
while True:
    if button_a.was_pressed():
        counter += 1
    draw_counter(counter)
