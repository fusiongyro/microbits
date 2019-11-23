from microbit import *
import radio

radio.on()

last_gesture = None
while True:
    current = accelerometer.current_gesture()
    if current in ['face up', 'face down'] and \
       last_gesture != current:
        last_gesture = current
        radio.send(current)
        print(current)
    sleep(10)
