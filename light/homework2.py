import spidev
import time
import RPi.GPIO as GPIO
import LED


delay = 2
ldr_channel = 0
global gGPIOnum

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000


def Setup(GPIOnum, frequency):
    global gGPIOnum
    GPIO.setmode(GPIO.BCM)
    gGPIOnum  = GPIOnum
    GPIO.setup(gGPIOnum, GPIO.OUT)

    gGPIOnum = GPIO.PWM(gGPIOnum, frequency)
    gGPIOnum.start(0)


def readadc(adcnum):
    if adcnum >7 or adcnum <0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

    
    

def max_min_normalization(input_data):
    new_data = (input_data - 420)/(1023-420)*(100)+0
    print(new_data)
    return new_data

def PWM(data):
    gGPIOnum.ChangeDutyCycle(data)
    time.sleep(0.1)

Setup(15, 100)
while True:

    ldr_value = readadc(ldr_channel)
    print("-----------------------------------")
    print("LDR Value: %d" % ldr_value)
    new_data = max_min_normalization(ldr_value)
    PWM(new_data)
    time.sleep(delay)
