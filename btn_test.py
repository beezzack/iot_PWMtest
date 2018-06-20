import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

btn = 4
gpio.setup(4,gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    starttime = time.time()
    while True:
        time.sleep(1)

        #if(gpio.input(btn) == 0):
        print(str(gpio.input(btn))+", "+str(time.time()-starttime))

except KeyboardInterrupt:
    pass

gpio.cleanup()