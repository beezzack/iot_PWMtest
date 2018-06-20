import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

btn = [4, 17]
gpio.setup(4,gpio.IN)

try:
    starttime = time.time()
    while True:
        time.sleep(1)

        #if(gpio.input(btn) == 0):
        print(str(gpio.input(btn[0]))+", "+str(time.time()-starttime))

except KeyboardInterrupt:
    pass

gpio.cleanup()