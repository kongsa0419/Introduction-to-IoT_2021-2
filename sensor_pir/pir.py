import RPi.GPIO as gpio
import time

pin = 25

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.IN)

try:
	while True:
		if gpio.input(pin) == True:
			print("Sensor on!")
			time.sleep(0.2)
		if gpio.input(pin) == False:
			print("Sensor off!")
			time.sleep(0.2)
except KeyboardInterrupt:
	gpio.cleanup()
