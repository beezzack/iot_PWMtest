import time
import RPi.GPIO as GPIO

DS = 21
ST_CP = 16
SH_CP = 20
MR = 4
GPIO.setmode(GPIO.BCM)
LED_list = [1,1,0,1,1,0,1,0]

def shriftout(byte):
    GPIO.output(ST_CP, 0)
    b = ''
    for x in range(8):
        bit = LED_list[x]
        GPIO.output(DS, bit)
        GPIO.output(SH_CP, 1)
        GPIO.output(SH_CP, 0)

    print(b[::-1])
    GPIO.output(STCP, 1)
if __name__ == '__main__':
    GPIO.setup(DS,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(ST_CP,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(SH_CP,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(MR,GPIO.OUT,initial = GPIO.HIGH)

    go()
        
