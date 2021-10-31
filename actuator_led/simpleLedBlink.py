import RPi.GPIO as gpio
import time

led_pin = 5

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

gpio.output(led_pin, True)
time.sleep(0.5)
gpio.output(led_pin, False)
time.sleep(0.5)
gpio.output(led_pin, True)
time.sleep(0.5)
gpio.output(led_pin, False)
time.sleep(0.5)

print("Blink Finished")
gpio.cleanup()
