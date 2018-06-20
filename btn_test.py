import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

btn = 4
gpio.setup(4,gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    while True:
        time.sleep(0.1)

        if(gpio.input(btn) == 0):
            print("press")

except KeyboardInterrupt:
    pass

gpio.cleanup()