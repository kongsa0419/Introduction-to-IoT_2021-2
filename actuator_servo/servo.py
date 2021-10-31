import RPi.GPIO as gpio
import time

pin = 18 # PWM pin

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

p = gpio.PWM(pin, 50)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5)
        time.sleep(1)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(10)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()
