import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from time import sleep





GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=14
GPIO_ECHO=15

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
#motor*****************/
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3,50)
pwm.start(0)
#GPIO.output(3, True)
#/********************************/
def SetAngle(angle):
    dutyCycle= 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)

def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER ,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

def get_speed():
    speed = 33100 + 26 * 60
    return speed

def distance(speed):
    send_trigger_pulse()

    while GPIO.input(GPIO_ECHO)==0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distancenum = (TimeElapsed*speed)/2

    return distancenum

if __name__ == '__main__':
    try:
        while True:
            speed = get_speed()
            dist = distance(speed)
            print("Measured Distance = %.1f cm" % dist)
    
            if dist>=14:
                SetAngle(0)
            elif dist > 12 and dist <= 14:
                SetAngle(30)
            elif dist > 10 and dist <= 12:
                SetAngle(60)
            elif dist > 8 and dist <= 10:
                SetAngle(90)
            elif dist > 6 and dist <= 8:
                SetAngle(120)
            elif dist > 4 and dist <= 6:
                SetAngle(150)
            else:
                SetAngle(180)
            time.sleep(1)
            
    except KeyboardInterrupt:
            print("Measurement stopped by User")
            GPIO.cleanup()
            pwm.stop()
