import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

btn = [4, 17]
for b in btn:
    gpio.setup(b,gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    starttime = time.time()
    while True:
        time.sleep(1)

        print(int(time.time() - starttime))
        print([gpio.input(b) for b in btn])

except KeyboardInterrupt:
    pass

gpio.cleanup()