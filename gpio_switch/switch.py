import RPi.GPIO as gpio
import time

switch_pin = 12

gpio.setmode(gpio.BCM)
gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)

def button():
    isClicked = False
    if gpio.input(switch_pin) == 0:
        isClicked = True
    return isClicked

try:
    while True:
        if button() == True:
            print("Switch On")
            time.sleep(0.5)
        else:
            print("Switch Off")
            time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()
    

