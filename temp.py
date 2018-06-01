from microbit import *

while True:
    display.scroll('{:4.1f}'.format(1.8 * temperature() + 32))
    sleep(2000)
