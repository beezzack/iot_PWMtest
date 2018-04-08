import pygame
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


def LED_on(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(GPIOnum, GPIO.HIGH)

def LED_off(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(GPIOnum, GPIO.LOW)


def setupPIM(GPIOnum):
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

counter = 0
def motion(GPIOnum):
    global counter

    if GPIO.input(GPIOnum):
        counter += 1
        print("Motion detected {0}".format(counter))
    else:
        print("Motion not detected")

try:
    setupPIM(14)
    GPIO.setup(5, GPIO.OUT)#R
    GPIO.setup(13, GPIO.OUT)#Y
    GPIO.setup(17, GPIO.OUT)#G
    GPIO.add_event_detect(14, GPIO.BOTH, callback=motion, bouncetime=100)
    while True:
        time.sleep(1)

except:
    GPIO.cleanup()
