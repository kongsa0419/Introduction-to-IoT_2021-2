import RPi.GPIO as gpio
import dht11
import time
import datetime

# initialize GPIO
gpio.setwarnings(True)
gpio.setmode(gpio.BCM)
gpio.cleanup()

# read data using pin 19
instance = dht11.DHT11(pin=19)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()
