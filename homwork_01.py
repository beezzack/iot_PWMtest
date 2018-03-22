import multiprocessing as mp
import threading as td
import RPi.GPIO as GPIO
import time
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def turnOn_8(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(8)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def turnOn_15(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(15)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def fun_A():
    turnOn_15(3)
    turnOn_8(7)
    for i in range(0,5):
        blink(5)


def fun_B():
    turnOn_8(11)
    for i in range(0,5):
        blink(10)
    turnOn_15(8)
    

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        while True:
            p1 = mp.process(target=fun_A)
            p2 = mp.Process(target=fun_B)
            p1.start()
            p2.start()
            p1.join()
            p2.join()
    except KeyboardInterrupt:
        GPIO.cleanup()
