import RPi.GPIO as GPIO
import time

global gGPIOnum
def Setup(gGPIOnum, frequency):
    GPIO.setmode{GPIO.BCM}
    gGPIOnum = GPIOnum
    GPIO.setup(gGPIOnum, GPIO.OUT)

    gGPIOnum = GPIO.PWM(gGPIOnum, frequency)
    gGPIOnum.start(0)

if __name__ == "__main__":
    try:
        Setup(2,100)
        while True:
            for dc in range(0,101,1):
                gGPIOnum,ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100,-1,1):
                gGPIOnum,ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
